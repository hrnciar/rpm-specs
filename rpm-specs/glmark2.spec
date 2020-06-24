%global commit0 0003eff782938daf852a70f6ca4cdf8fafd02854
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global commitdate0 20180717

Name:		glmark2
Version:	2017.07
Release:	4.%{commitdate0}git%{shortcommit0}%{?dist}
Summary:	Benchmark for OpenGL 2.0


License:	GPLv3
URL:		https://github.com/glmark2/glmark2
Source0:	%{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz


## The bellow sources are carried by Fedora package maintaners


##
## .desktop files
##

# 9a43f39f0ddfc91e758e7d7cc44169df30f432b85e668ac135eb38e5dbaa48d8
Source1:	%{name}.desktop

# 5f4c57f5d183ab1b989f293bbc2a6abc27d54f6f796a62318fe7519cc9311a21
Source2:	%{name}-es2.desktop

# ca9e822c62d415052cb27474bfa6ac2f700409bfbeffe9450444b9ef2f5ee246
Source8:	%{name}-drm.desktop

# 74d8b8939dbb9c704c355aa76c10e71bb85adf500ebe3dfa5049d29c52876d05
Source9:	%{name}-es2-drm.desktop



##
## .desktop pixmap icons
##


# de1229366912806f838409c7ff315be5cc48c6e659d78dfd80d0c5db4dcede1d
Source3:	%{name}.png

# aabcddd0c23d20daf0ed024ae4e7b925ec2fb63bb656843d7180904093a8020e
Source4:	%{name}-es2.png

# 12262d758152ac7c404e8f7173024366ebf4f326935584c1b147c5f3ce1341bf
Source12:	%{name}-drm.png

# 12262d758152ac7c404e8f7173024366ebf4f326935584c1b147c5f3ce1341bf
Source13:	%{name}-es2-drm.png


##
## gimp icon sources (not packaged into final rpm, just source rpm)
##

# 1e96f5291318a9c466eed0435ad0e740c789a9b418476807b7253ce0d88b5421
Source5:	%{name}.xcf

# 163b7db2a293e1e86a34c6f84294bb1f54e313ef983fff511a4fe1abca9acd5f
Source6:	%{name}-es2.xcf

# 7ab4b18107ecf3140493f7eeaf2374f8de82bbcb82fe98d58e444b174266f1f7
Source10:	%{name}-drm.xcf

# cc25e28b8c5db4f03e18b95d557323ab09d5a9849946e41e45ba11e3b6df13bb
Source11:	%{name}-es2-drm.xcf



##
## appdata - glmark2 only!
##

# 2d5b3e7c9380d068598f272b2f5b55ca736fa157fd205246a86c2473e08577d4
Source7:	%{name}.appdata.xml


##
## BRs
##

BuildRequires:	gcc-c++
BuildRequires:	libjpeg-devel
BuildRequires:	pkgconfig(libpng12)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	python2-devel
BuildRequires:	desktop-file-utils
BuildRequires:	appdata-tools
BuildRequires:	waf



Requires:	%{name}-common = %{version}-%{release}

%description
Glmark2 is a benchmark for OpenGL 2.0.




## 
##  sub-package
##  The noarch sub-package is easier on the mirrors.
##  One package for common noarch data shared with all architectures.
##  


%package common
Summary:	Models, Textures, and Shaders for GLmark2 Benchmark suite
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}
%description common
Common graphical assets for Glmark2 benchmark suite




%prep
%autosetup -p1 -n %{name}-%{commit0}

# Remove bundled libraries!
rm -r src/libjpeg-turbo src/libpng
rm -r waf waflib

%build
%{_bindir}/waf configure \
  --with-flavors="x11-gl,x11-glesv2,drm-gl,wayland-gl,wayland-glesv2,drm-glesv2" \
  --prefix=%{_usr} \

%{_bindir}/waf -v %{?_smp_mflags}


%install
%{_bindir}/waf install -v --destdir=%{buildroot}


## The .desktop files
desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications %{SOURCE8}

desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications %{SOURCE9}


## The ICON files
%{__install} -vd	"%{buildroot}%{_datadir}/pixmaps/"
%{__install} -vp	%{SOURCE3} \
					%{SOURCE4} \
					%{SOURCE12} \
					%{SOURCE13} \
					"%{buildroot}%{_datadir}/pixmaps/"

## The appdata
%{__install} -vd "%{buildroot}%{_datadir}/appdata/"
%{__install} -vp %{SOURCE7} "%{buildroot}%{_datadir}/appdata/"


## Upstream presently does not have any %%check's 
## Here we validate .appdata.xml files, but make erros non-fatal
%check
#appdata-validate %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml || true
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml || :


%files
## the x11 opengl benchmark
%doc NEWS README
%license COPYING COPYING.SGI
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz


## x11 Opengl benchmark DRM
%{_datadir}/applications/%{name}-drm.desktop
%{_datadir}/pixmaps/%{name}-drm.png
%{_bindir}/%{name}-drm
%{_mandir}/man1/%{name}-drm.1.gz


## Opengl ES 2 benchmark
%{_datadir}/applications/%{name}-es2.desktop
%{_datadir}/pixmaps/%{name}-es2.png
%{_bindir}/%{name}-es2
%{_mandir}/man1/%{name}-es2.1.gz


## Opengl ES 2 benchmark DRM
%{_datadir}/applications/%{name}-es2-drm.desktop
%{_datadir}/pixmaps/%{name}-es2-drm.png
%{_bindir}/%{name}-es2-drm
%{_mandir}/man1/%{name}-es2-drm.1.gz

## Opengl ES 2 benchmark wayland
%{_bindir}/glmark2-es2-wayland
%{_mandir}/man1/glmark2-es2-wayland.1.gz

## Opengl benchmark wayland
%{_bindir}/glmark2-wayland
%{_mandir}/man1//glmark2-wayland.1.gz


%files common
## assets: models, shaders, textures
%{_datadir}/%{name}/



%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2017.07-4.20180717git0003eff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017.07-3.20180717git0003eff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017.07-2.20180717git0003eff
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Nicolas Chauvet <kwizart@gmail.com> - 2017.07-1.20180407git0003eff
- Bump to 2017.07 snapshot
- Switch to github
- Switch to system waf

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2014.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2014.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2014.03-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2014.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2014.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri May 20 2016 Jonathan Wakely <jwakely@redhat.com> - 2014.03-6
- Fixed description of glmark2-common subpackage

* Thu May 19 2016 Jonathan Wakely <jwakely@redhat.com> - 2014.03-5
- Fixed build with GCC 6 (#1307539)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2014.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2014.03-3
- Rebuilt for GCC 5 C++11 ABI change

* Sun Jan 04 2015 Jon Disnard <jdisnard@gmail.com> 2014.03-2
- Use current appdata validation standards.

* Fri Jan 02 2015 Jon Disnard <jdisnard@gmail.com> 2014.03-1
- Now using upstream 2014.03
- re-jiggered waf configure per upstream

* Sun Feb 23 2014 Jon Disnard <jdisnard@gmail.com> 2012.12-3
- fix %%files datadir ownership
- remove redundant .desktop validation checks
- add transitive dep in -common sub-package
- Remove bundled libraries per package guidelines
- Move waf ./configure to %%build phase


* Sat Feb 01 2014 Jon Disnard <jdisnard@gmail.com> 2012.12-2
- Make appdata-validate informative, not imperative.

* Sat Feb 01 2014 Jon Disnard <jdisnard@gmail.com> 2012.12-2
- Package review fixes

* Sun Jan 26 2014 Jon Disnard <jdisnard@gmail.com> 2012.12-1
- Inception

