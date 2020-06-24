# TODO: write AppData manifest

# LTO
%global optflags %{optflags} -flto
%global build_ldflags %{build_ldflags} -flto

Name:           vokoscreenNG
Version:        3.0.4
Release:        1%{?dist}
Summary:        User friendly Open Source screencaster

License:        GPLv2
URL:            https://github.com/vkohaupt/vokoscreenNG
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  intltool
#BuildRequires:  libappstream-glib
BuildRequires:  cmake(Qt5)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(gstreamermm-1.0)
BuildRequires:  pkgconfig(x11)

%description
VokscreenNG is a user friendly Open Source screencaster for Linux and Windows.
The new name is now vokoscreenNG and has been rewritten from scratch.


%prep
%autosetup -p1
mkdir -p src/%{_target_platform}


%build
pushd src/%{_target_platform}
%qmake_qt5 ..
popd
%make_build -C src/%{_target_platform}


%install
%make_install -C src/%{_target_platform}
install -m 0755 -Dp src/%{_target_platform}/%{name} \
    %{buildroot}%{_bindir}/%{name}

# Desktop file
install -m 0644 -Dp src/applications/%{name}.desktop \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

# Icon
install -m 0644 -Dp src/applications/%{name}.png \
    %{buildroot}%{_datadir}/pixmaps/%{name}.png


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license COPYING
%doc README.md ToDo.txt INSTALL
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png


%changelog
* Wed Apr 29 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.0.4-1
- Update to 3.0.4

* Tue Mar 31 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.0.3-1
- Update to 3.0.3

* Wed Mar 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.0.2-1
- Update to 3.0.2

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 03 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 3.0.0-2
- Initial package
