Name:		grafx2
Version:	2.5
Release:	8%{?dist}
Summary:	A bitmap paint program specialized in 256 color drawing
URL:		http://grafx2.chez.com/
# recoil is GPLv2+, grafX2 is GPLv2 only
# two files are CeCILL v2
# src/libraw2crtc.*
License:	GPLv2 and CeCILL
Source0:	https://gitlab.com/GrafX2/grafX2/-/archive/v2.5/grafX2-v%{version}.tar.bz2
Source1:	https://sourceforge.net/projects/recoil/files/recoil/4.2.0/recoil-4.2.0.tar.gz
Source2:	grafx2.appdata.xml
# Fix src/Makefile to use $(CP) everywhere
Patch0:		grafX2-v2.5-cp-fix.patch
# Fix src/Makefile to create all the directories during make install
Patch1:		grafX2-v2.5-moar-dirs.patch
BuildRequires:	SDL-devel, SDL_image-devel, SDL_ttf-devel, zlib-devel
BuildRequires:	libpng-devel, freetype-devel, libX11-devel, lua-devel, gcc, make
BuildRequires:	fontconfig-devel, desktop-file-utils
Provides:	bundled(recoil) = 4.2.0

%description
GrafX2 is a bitmap paint program inspired by the Amiga programs ​Deluxe Paint
and Brilliance. Specialized in 256-color drawing, it includes a very large
number of tools and effects that make it particularly suitable for pixel
art, game graphics, and generally any detailed graphics painted with a
mouse.

%prep
%setup -q -n grafX2-v%{version}
%patch0 -p1 -b .cpa
%patch1 -p1 -b .moardirs

sed -i 's|-O$(OPTIM)|%{optflags}|g' src/Makefile
sed -i 's|$(LUALOPT)|$(LUALOPT) %{build_ldflags}|g' src/Makefile

iconv -f iso8859-1 -t utf8 doc/tech_eng.txt -o doc/tech_eng.txt.utf8
touch -r doc/tech_eng.txt doc/tech_eng.txt.utf8
mv doc/tech_eng.txt.utf8 doc/tech_eng.txt

mkdir -p 3rdparty/archives/
cp -a %{SOURCE1} 3rdparty/archives/

%build
cd src
make %{?_smp_mflags}

%install
cd src
make DESTDIR=%{buildroot} prefix=%{_prefix} CP="cp -a" install

# install appdata file
mkdir -p %{buildroot}%{_metainfodir}
cp %{SOURCE2} %{buildroot}%{_metainfodir}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/grafx2.desktop

%files
%license LICENSE
%doc doc/README.txt doc/tech_eng.txt doc/quickstart.rtf
%{_bindir}/grafx2
%{_metainfodir}/grafx2.appdata.xml
%{_datadir}/applications/grafx2.desktop
%{_datadir}/grafx2/
%{_datadir}/icons/grafx2*

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Tom Callaway <spot@fedoraproject.org> - 2.5-2
- fix license tag
- add appdata file
- comment patches

* Tue Jun 12 2018 Tom Callaway <spot@fedoraproject.org> - 2.5-1
- initial package
