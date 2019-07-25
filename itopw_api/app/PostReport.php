<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class PostReport extends Model
{
    protected $table = "post_reports_postreport";

    protected $fillable = ['content', 'post_id', 'user_id'];

    public function posts()
    {
    	return $this->belongsTo('App\Post');
    }
}
