Name:       eureka
Version:    1.27
Release:    2%{?dist}
Summary:    A cross-platform map editor for the classic DOOM games

%global nodotver %(echo %{version} | tr -d '.')

License:    GPLv2
URL:        http://eureka-editor.sourceforge.net
Source0:    http://downloads.sourceforge.net/project/eureka-editor/Eureka/%{version}/%{name}-%{nodotver}-source.tar.gz
Source1:    eureka.desktop

BuildRequires:  gcc-c++
BuildRequires:  fltk-devel
BuildRequires:  libXft-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  xdg-utils
BuildRequires:  libGL-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ImageMagick

%description
Eureka is a cross-platform map editor for the classic DOOM games.

It started when the ported the Yadex editor to a proper GUI toolkit, namely
FLTK, and implemented a system for multi-level Undo / Redo. These and other
features have required rewriting large potions of the existing code, and adding
lots of new code too. Eureka is now an independent program with its own
work-flow and its own quirks.


%prep
%setup -q -n %{name}-%{version}-source
# omit stripping the binaries and prevent installing as root
%{__sed} -i \
  -e "s|install: stripped|install:|" \
  -e "s|-o root||g" \
  Makefile


%build
LIBS+=-lX11 make %{?_smp_mflags} OPTIMISE="$RPM_OPT_FLAGS"


%install
%{__mkdir_p} %{buildroot}%{_bindir}
make install PREFIX="%{buildroot}%{_prefix}"

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
convert misc/eureka.ico %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/eureka.png

desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
%files
%license GPL.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/128x128/apps/eureka.png
%{_datadir}/applications/*.desktop
%doc AUTHORS.txt CHANGES.txt README.txt TODO.txt


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.27-1
- 1.27

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.24-1
- 1.24

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 1.21-1
- Bump to latest version (1.21)
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.00-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.00-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 15 2015 Rex Dieter <rdieter@fedoraproject.org> 1.00-5
- rebuild (fltk)

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.00-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Sep 8 2013 Jay Greguske <brolem@gmail.com> 1.00-3
- add changes from Ralf Corsepius during review

* Thu Sep 5 2013 Jay Greguske <brolem@gmail.com> 1.00-2
- incorporate a few suggestions from Christopher Meng

* Mon Aug 26 2013 Jay Greguske <brolem@gmail.com> 1.00-1
- Initial import from upstream 1.00 release
