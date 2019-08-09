<?php
function slug_convert($data)
{
    $data['slug'] = \Illuminate\Support\Str::slug($data['name'], '-');
    return $data;
}
?>