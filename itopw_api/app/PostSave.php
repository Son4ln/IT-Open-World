<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class PostSave extends Model
{
    protected $table = "save_posts_saveposts";

    protected $fillable = ['post_id', 'user_id'];

    public function posts()
    {
    	return $this->belongsTo('App\Post');
    }
}
