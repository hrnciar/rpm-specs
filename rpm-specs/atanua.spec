%global commit 2a58d7fb349de3062dea61b0fb072f8e7370dde6
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           atanua
Version:        1.3.141220
Release:        13%{?dist}
Summary:        Real Time Logic Simulator

License:        zlib and Bitstream Vera
# atanua: zlib
# vera fonts: Bitstream Vera
URL:            http://sol.gfxile.net/atanua/
Source0:        https://github.com/jarikomppa/atanua/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Source1:        http://sol.gfxile.net/zip/atanua141220.zip
Source2:        atanua.desktop
Source3:        icon.png
Source4:        x-atanua-simulation.xml
Source5:        atanua.appdata.xml
Source6:        atanua.png
Source7:        atanua-2.png

# https://github.com/jarikomppa/atanua/pull/4
Patch1:         0001-Don-t-crash-on-file-open-failures.patch
Patch2:         0002-Check-the-correct-pointer-for-NULL.patch
Patch3:         0003-A-bit-better-error-handling.patch
Patch4:         0004-Fix-Linux-build.patch
Patch5:         0005-Allow-builds-without-bundling-the-libraries.patch
Patch6:         0006-Allow-overriding-the-data-directory-on-build.patch
Patch7:         0007-Rename-TiXmlNode-ELEMENT-and-TEXT.patch
Patch8:         atanua-fix-build.patch

BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  tinyxml-devel
BuildRequires:  stbi-devel
BuildRequires:  GLee-devel
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib

%description
Atanua is a real-time logic simulator, designed to help in learning of basic 
boolean logic and electronics. It uses OpenGL hardware-accelerated rendering 
and a custom UI designed for a fast workflow and a very low learning curve, 
letting the students concentrate on learning the subject instead of spending 
time learning the tool.


%prep
%setup -q -n %{name}-%{commit} -a1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1


%build
make %{?_smp_mflags} CFLAGS='%{optflags} -DDATADIR=\"%{_datadir}/atanua\" -DGL_GLEXT_PROTOTYPES' \
        CC=%{__cc} CXX=%{__cxx} UNBUNDLE=1


%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}
install -d %{buildroot}%{_datadir}/mime/packages
install -d %{buildroot}%{_datadir}/pixmaps
install -d %{buildroot}%{_datadir}/appdata

install atanua %{buildroot}%{_bindir}
cp -a data %{buildroot}%{_datadir}/atanua
install -pm644 %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/atanua.png

install -pm644 %{SOURCE4} %{buildroot}%{_datadir}/mime/packages/
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

install -pm644 %{SOURCE5} %{buildroot}%{_datadir}/appdata/


%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%files
%{_bindir}/atanua
%{_datadir}/atanua
%{_datadir}/applications/atanua.desktop
%{_datadir}/mime/packages/x-atanua-simulation.xml
%{_datadir}/pixmaps/atanua.png
%{_datadir}/appdata/atanua.appdata.xml
%doc readme.md
%license LICENSE
%license data/vera_copyright.txt


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.141220-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 01 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.3.141220-12
- Fix build and run with LD_BIND_NOW

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.141220-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.141220-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.141220-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 14 2018 Filipe Rosset <rosset.filipe@gmail.com> - 1.3.141220-8
- rebuilt to fix FTBFS

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.141220-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.141220-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 29 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.3.141220-5
- Use a bigger icon for appstream

* Fri Apr 29 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.3.141220-4
- Correct AppStream component type

* Fri Apr 29 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.3.141220-3
- Add AppStream metadata

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.141220-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.3.141220-1
- Initial packaging
