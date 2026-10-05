// =============================================================================
//  Portal Brand Tokens framework v1.0 - UI actions on sp_theme (server-side)
//  Condition (both): gs.hasRole('admin') || gs.hasRole('sp_admin')
// =============================================================================


// --- "Sync Next Experience theme" ---------------------------------------------
// sys_ui_action 462559742b734350ff68f76a6e91bf60 . action_name portal_brand_tokens_ux_sync
// Form button, order 200, show on insert + update.

// Portal Brand Tokens framework v1.0
// Generates (or refreshes) the matching Next Experience theme from this theme's palette.
current.update();
try {
    var result = new PortalBrandTokensUx().sync(current.getUniqueValue());
    gs.addInfoMessage('Next Experience theme synced: ' + result.base_tokens_written + ' colour tokens and ' +
        result.font_tokens_written + ' font tokens written to "' + current.getValue('name') + ' (generated UX theme)".');
    if (result.warnings.length)
        gs.addErrorMessage('Check the palette: ' + result.warnings.join('; '));
} catch (e) {
    gs.addErrorMessage('Next Experience theme sync failed: ' + e.message);
}
action.setRedirectURL(current);


// --- "Clone theme with includes" ----------------------------------------------
// sys_ui_action f23ad9f82bf7cf10a5feffb86e91bfb4 . action_name portal_brand_tokens_clone
// Form link + context menu, order 210, show on update only.

// Portal Brand Tokens framework v1.0
// Copies this theme with its CSS/JS includes and images, then opens the copy.
try {
    var id = new PortalBrandTokensUx().cloneTheme(current.getUniqueValue(), 'Copy of ' + current.getValue('name'));
    var copy = new GlideRecord('sp_theme');
    copy.get(id);
    gs.addInfoMessage('Theme copied with its includes. Next: rename it, edit Section 1 of CSS Variables, ' +
        'then use "Sync Next Experience theme".');
    action.setRedirectURL(copy);
} catch (e) {
    gs.addErrorMessage('Clone failed: ' + e.message);
    action.setRedirectURL(current);
}
