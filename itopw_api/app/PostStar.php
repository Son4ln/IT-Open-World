<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class PostStar extends Model
{
    protected $table = "post_stars_poststars";

    protected $fillable = ['post_id', 'user_id'];

    public function posts()
    {
    	return $this->belongsTo('App\Post');
    }
}
