# Makefile manages to ignore hardened_build
#global _hardened_build 1

Summary: FUSE filesystem to transcode FLAC to MP3 on the fly
Name: mp3fs
Version: 0.91
Release: 11%{dist}
License: GPLv3+ and GFDL
Source0: https://github.com/khenriks/mp3fs/releases/download/v%{version}/mp3fs-%{version}.tar.gz
#Patch0: mp3fs.patch
URL: http://khenriks.github.com/mp3fs/
# While mp3fs does encode to MP3, it is a consumer, not a provider
#Provides: mp3encoder
# While mp3fs does not strictly require the fuse cli (which does not provide
# the fuse libraries), mp3fs is fairly useless without it.
Requires: fuse
BuildRequires: fuse-devel lame-devel flac-devel libid3tag-devel gcc-c++

%description
MP3FS is A read-only FUSE file-system which trans-codes audio formats (currently
FLAC) to MP3 on the fly when opened and read. This was written to enable me to
use my FLAC collection with software and/or hardware which only understands
MP3. e.g. "GMediaServer" to a Netgear MP101 mp3 player.

It is also a novel alternative to traditional mp3 encoder applications. Just
use your favorite file browser to select the files you want encoded and copy
them somewhere!

%prep
%setup -q 
#patch0 -p1 -b .sdg

%build
%configure
%{make_build} LDFLAGS="$RPM_LD_FLAGS -lm" V=1

%install
%make_install

%files
%{!?_licensedir:%global license %%doc}
%license COPYING COPYING.DOC
%doc NEWS ChangeLog README.md INSTALL.md
%{_bindir}/%{name}
%{_mandir}/man1/*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.91-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun  4 2018 Stuart Gathman <stuart@gathman.org> 0.91-7
- Rebuilt to move from rpmfusion to Fedora, since dependencies have moved

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.91-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.91-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.91-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 26 2016 Stuart Gathman <stuart@gathman.org> 0.91-3
- Remove space from Summary:
- Include $RPM_LD_FLAGS in LDFLAGS
- Removed mp3encoder provides, not useful apparently

* Tue Oct 18 2016 Stuart Gathman <stuart@gathman.org> 0.91-2
- Clean up to resubmit to rpmfusion.

* Sat Jan 24 2015 Stuart Gathman <stuart@gathman.org> 0.91-1
- Update to 0.91 on Fedora 19

* Wed Oct 10 2012 Stuart Gathman <stuart@gathman.org> 0.32-1
- Update to 0.32 on Fedora 16

* Tue Jun 29 2010 Stuart Gathman <stuart@gathman.org> 0.20-1
- Update to 0.20 on Fedora 12

* Fri Oct 19 2007 Stuart Gathman <stuart@gathman.org> 0.13-1
- Update to 0.13 on Centos5

* Fri Oct 19 2007 Stuart Gathman <stuart@gathman.org> 0.11-1
- Update to 0.11 on Centos5

* Wed Nov 22 2006 Stuart Gathman <stuart@gathman.org> 0.03-2
- Rebuild with fuse-2.6

* Wed Nov  1 2006 Stuart Gathman <stuart@gathman.org> 0.03-1
- RPM 
