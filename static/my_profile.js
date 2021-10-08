console.log('hello world')

const toFollowModalBody = document.getElementById('to-follow-modal-body')
const toFollowBtn = document.getElementById('to-follow-btn')
const spinnerBox = document.getElementById('spinner-box')
let toFollowLoaded = false

console.log(toFollowModalBody)
console.log(spinnerBox)

toFollowBtn.addEventListener('click', ()=>{
$.ajax({
	type: 'GET',
	url: '/profiles/my-profile-json/',
	success: function(response){
		if(!toFollowLoaded) {
			const pfData = response.pf_data
			console.log(pfData)
			setTimeout(()=>{
				spinnerBox.classList.add('not-visible')
				pfData.forEach(el=>{
					toFollowModalBody.innerHTML +=
						`<div class="row mb-2 align-items-center>
							<div class="col-3">
							    <div class="text-muted">${el.user}</div>
							</div>
							<div class="col text-right">
								<button class="btn btn-success">Follow</button>
							</div>	
						 </div>`
				})
			}, 2000)
		}

		toFollowLoaded = true
	},
	error: function(error){
		console.log(error)
	}
 })

})