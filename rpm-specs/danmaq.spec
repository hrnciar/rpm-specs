%global icondir %{_datadir}/icons/hicolor
%global reponame danmaQ

Name:		danmaq
Version:	0.2.3.1
Release:	8%{?dist}
Summary:	A small client side Qt program to play danmaku on any screen

License:	GPLv3
URL:		https://github.com/TUNA/%{reponame}
Source0:        %{url}/archive/v%{version}/%{reponame}-v%{version}.tar.gz

BuildRequires:	qt5-qtx11extras-devel
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-devel
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:  libXext-devel

%description
DanmaQ is a small client side Qt program to play danmaku on any screen.

%prep
%setup -q -n %{reponame}-%{version}

%build
mkdir build && cd build
%cmake ..
# Since 0.2.3 it cannot be built in parallel. So use make instead of macro.
make

%install
# install 
pushd build
%make_install
#install -Dm 0755 build/src/%{reponame} %{buildroot}%{_bindir}/%{reponame}
popd

# icon files
install -Dm0644 src/icons/statusicon.ico    %{buildroot}%{_datadir}/pixmaps/statusicon.ico
install -Dm0644 src/icons/statusicon.png    %{buildroot}%{_datadir}/pixmaps/statusicon.png
install -Dm0644 src/icons/statusicon_disabled.png    %{buildroot}%{_datadir}/pixmaps/statusicon_disabled.png
install -Dm0644 src/icons/statusicon.svg %{buildroot}%{icondir}/scalable/apps/statusicon.svg
install -Dm0644 src/resource/danmaQ.desktop %{buildroot}%{_datadir}/applications/%{reponame}.desktop
install -Dm0644 src/resource/danmaQ.png    %{buildroot}%{_datadir}/pixmaps/danmaQ.png
install -Dm0644 src/resource/danmaQ.svg %{buildroot}%{icondir}/scalable/apps/danmaQ.svg


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{reponame}.desktop

%post
/bin/touch --no-create %{_datadir}/icons/scalable &>/dev/null ||:

%postun
if [ $1 -eq 0 ]; then
  /bin/touch --no-create %{_datadir}/icons/scalable &>/dev/null ||:
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/scalable &>/dev/null ||:
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/scalable &>/dev/null ||:

%files
%doc README.md
%license LICENSE
%{_bindir}/%{reponame}
%{_mandir}/man1/%{reponame}.1.gz
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/%{reponame}.desktop

%changelog
* Sun Feb 09 2020 Zamir SUN <sztsian@gmail.com> - 0.2.3.1-8
- Fix FTBFS in Fedora 32
- Resolves 1799269

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.3.1-2
- Remove obsolete scriptlets

* Sun Nov 19 2017 Zamir SUN <zsun@fedoraproject.org> - 0.2.3.1-1
- Update to upstream version 0.2.3.1

* Sat Jul 29 2017 Zamir SUN <zsun@fedoraproject.org> - 0.2-1
- Change version to newest upstream tag

* Sat Jul 15 2017 Zamir SUN <zsun@fedoraproject.org> - 0-0.1.20170715git
- Initial with danmaQ git ab838667d53c71c6cf8ac94dd109fcd009460530
