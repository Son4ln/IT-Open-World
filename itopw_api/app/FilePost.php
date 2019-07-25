<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class FilePost extends Model
{
    protected $table = "post_files_postfiles";

    protected $fillable = ['file', 'name', 'size', 'mime', 'post_id'];

    public function posts()
    {
    	return $this->belongsTo('App\Post');
    }
}
