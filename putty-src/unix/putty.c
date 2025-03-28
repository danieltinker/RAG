/*
 * Unix PuTTY main program.
 */

#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <assert.h>
#include <unistd.h>
#include <gtk/gtk.h>
#include <gdk/gdk.h>

#define MAY_REFER_TO_GTK_IN_HEADERS

#include "putty.h"
#include "ssh.h"
#include "storage.h"

#include "gtkcompat.h"

#ifndef NOT_X_WINDOWS
#include <gdk/gdkx.h>
#endif

/*
 * Stubs to avoid pty.c needing to be linked in.
 */
const bool use_pty_argv = false;
char **pty_argv;                       /* never used */
char *pty_osx_envrestore_prefix;

/*
 * Clean up and exit.
 */
void cleanup_exit(int code)
{
    /*
     * Clean up.
     */
    sk_cleanup();
    random_save_seed();
    exit(code);
}

const struct BackendVtable *select_backend(Conf *conf)
{
    const struct BackendVtable *vt =
        backend_vt_from_proto(conf_get_int(conf, CONF_protocol));
    assert(vt != NULL);
    return vt;
}

void initial_config_box(Conf *conf, post_dialog_fn_t after, void *afterctx)
{
    char *title = dupcat(appname, " Configuration");
    create_config_box(title, conf, false, 0, after, afterctx);
    sfree(title);
}

const bool use_event_log = true, new_session = true, saved_sessions = true;
const bool dup_check_launchable = true;

/*
 * X11-forwarding-related things suitable for Gtk app.
 */

char *platform_get_x_display(void) {
    const char *display;
#ifndef NOT_X_WINDOWS
    /* Try to take account of --display and what have you. */
    if (!GDK_IS_X11_DISPLAY(gdk_display_get_default()) ||
        !(display = gdk_get_display()))
#endif
        /* fall back to traditional method */
        display = getenv("DISPLAY");
    return dupstr(display);
}

const bool share_can_be_downstream = true;
const bool share_can_be_upstream = true;

const unsigned cmdline_tooltype =
    TOOLTYPE_HOST_ARG |
    TOOLTYPE_PORT_ARG |
    TOOLTYPE_NO_VERBOSE_OPTION;

void setup(bool single)
{
    sk_init();
    enable_dit();
    settings_set_default_protocol(be_default_protocol);
    /* Find the appropriate default port. */
    {
        const struct BackendVtable *vt =
            backend_vt_from_proto(be_default_protocol);
        settings_set_default_port(0); /* illegal */
        if (vt)
            settings_set_default_port(vt->default_port);
    }
}
