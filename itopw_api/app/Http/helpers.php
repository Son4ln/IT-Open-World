<?php
function slug_convert($str)
{
    return \Illuminate\Support\Str::slug($str, '-');
}
?>