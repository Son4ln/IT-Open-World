<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Comment extends Model
{
    protected $table = "comments_comment";

    protected $fillable = ['content', 'creator_id', 'last_modified_by_id', 'parent_id', 'post_id', 'user_id'];

    protected $casts = [
    	'created_at' => 'datetime',
    	'updated_at' => 'datetime',
    	'deleted_at' => 'datetime'
    ];

    public function posts()
    {
    	return $this->belongsTo('App\Post');
    }

    public function users()
    {
    	return $this->belongsTo('App\User');
    }
}
