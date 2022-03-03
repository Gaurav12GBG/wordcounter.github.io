
saveState = [];
var saveI = 0;

$('.inputRegion').on("keydown", function (event) {
    if (event.which == " ".charCodeAt(0)) {
        saveState.push($(this).val());
        saveI = saveState.length - 1;
        debug();
    }
});

function triggerUndo() {
    if (saveI >= 0) {
        saveI--;
        $(".inputRegion").val(saveState[saveI]);
    }
    debug();
}

function triggerRedo() {
    if (saveI < saveState.length) {
        saveI++;
        $(".inputRegion").val(saveState[saveI]);
    }
    debug();
}

function debug() {
    return;
    //removed, used for debugging.
    console.log(saveI);
    console.log(saveState);
}