%global fver v.%{version}

Name: ags
Summary: Engine for creating and running videogames of adventure (quest) genre
Version: 3.4.4.2
URL:     http://www.adventuregamestudio.co.uk/site/ags/
Release: 2%{?dist}
Source0: https://github.com/adventuregamestudio/ags/archive/%{fver}/ags-%{fver}.tar.gz
# unbundle alfont
Patch0:  %{name}-use-system-alfont.patch
# unbundle allegro
Patch1:  %{name}-use-system-allegro.patch
License: Artistic 2.0 and BSD and Giftware and LGPLv2+ and Public Domain and zlib
BuildRequires: alfont-devel
BuildRequires: allegro-devel
BuildRequires: dumb-devel
BuildRequires: freetype-devel
BuildRequires: gcc-c++
BuildRequires: libogg-devel
BuildRequires: libtheora-devel
BuildRequires: libvorbis-devel
BuildRequires: libXext-devel
BuildRequires: libXxf86vm-devel
# https://web.archive.org/web/20050323070052/http://www.inp.nsk.su/~bukinm/dusty/aastr/ (Giftware)
# dead upstream, might be possible to use aastr2:
# https://www.allegro.cc/resource/Libraries/Graphics/AASTR2
Provides: bundled(aastr) = 0.1.1
# https://web.archive.org/web/20060518092445/http://nekros.freeshell.org/delirium/alogg.html (BSD)
# dead upstream, internals are used, not trivial to unbundle
Provides: bundled(AllegroOGG) = 1.0.3
# https://web.archive.org/web/20050305175733/http://nekros.freeshell.org/delirium/almp3.php (LGPLv2+)
# dead upstream, bundles parts of old mpg123, not trivial to separate
Provides: bundled(almp3) = 2.0.5
# http://kcat.strangesoft.net/apeg.html (Public Domain)
Provides: bundled(apeg) = 1.2.1
# https://web.archive.org/web/20090403045142/http://www.hiend3d.com/hq2x.html (LGPLv2+)
# dead upstream
Provides: bundled(hq2x3x)
# https://web.archive.org/web/20040104090747/http://www.alphalink.com.au/~tjaden/libcda/index.html (zlib)
# dead upstream
Provides: bundled(libcda) = 0.5

%description
Adventure Game Studio (AGS) - is the IDE and the engine meant for creating and
running videogames of adventure (aka "quest") genre. It has potential, although
limited, support for other genres as well.

Originally created by Chris Jones back in 1999, AGS was opensourced in 2011 and
since continued to be developed by contributors.

%prep
%setup -q -n %{name}-%{?commit:%{commit}}%{!?commit:%{fver}}
%patch0 -p1 -b .alfont
%patch1 -p1 -b .allegro
# delete unused bundled stuff
pushd Common/libinclude
rm -r OGG
rm -r theora
rm -r vorbis
rm aldumb.h
rm alfont{,dll}.h
rm dumb.h
popd
pushd Common/libsrc
rmdir googletest
popd
pushd Engine/libsrc
rm -r allegro-4.2.2-agspatch
rm -r alfont-2.0.9
rm -r dumb-0.9.2
popd
iconv -o Changes.txt.utf-8 -f iso8859-1 -t utf-8 Changes.txt && \
touch -r Changes.txt Changes.txt.utf-8 && \
mv Changes.txt.utf-8 Changes.txt

%build
%set_build_flags
%make_build V=1 -C Engine

%install
make V=1 -C Engine PREFIX=%{buildroot}%{_prefix} install

%files
%license License.txt
%doc Changes.txt Copyright.txt OPTIONS.md README.md
%{_bindir}/ags

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 09 2019 Dominik Mierzejewski <rpm@greysector.net> - 3.4.4.2-1
- use upstream source directly, offending files were removed upstream

* Wed Oct 02 2019 Dominik Mierzejewski <rpm@greysector.net> - 3.4.4.1-1
- initial Fedora package of 3.4.4.1 release
- remove non-free Engine/libsrc/libcda-0.5/{bcd.doc,djgpp.c} from tarball
- convert Changes.txt to UTF-8
