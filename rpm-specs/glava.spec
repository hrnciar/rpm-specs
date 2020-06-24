Name:           glava
Version:        1.6.3
Release:        3%{?dist}
Summary:        OpenGL audio spectrum visualizer

License:        GPLv3 and MIT
URL:            https://github.com/wacossusca34/glava
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Fedora-specific
Patch0001:      0001-Make-build-reproducible-and-verbose.patch

BuildRequires:  gcc
BuildRequires:  glfw-devel >= 3.1
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  libX11-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXext-devel
BuildRequires:  libXrender-devel
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python3dist(glad)
BuildRequires:  xorg-x11-proto-devel

%description
GLava is an OpenGL audio spectrum visualizer primarily used for desktop windows
or backgrounds. Multiple visualization styles are provided and new ones may be
written in GLSL. Development is active, and reporting issues is encouraged.

See https://github.com/wacossusca34/glava/wiki for more documentation.


%prep
%autosetup -p1

# Remove bundled glad files.
rm glad.?


%build
%set_build_flags
make PYTHON=%{__python3} glad
%make_build GLAVA_VERSION='\"%{version}\"' ENABLE_GLFW=1 SHADERDIR=%{_datadir}/glava/


%install
%make_install SHADERDIR=%{_datadir}/glava


%files
%doc README.md
%license LICENSE LICENSE_ORIGINAL
%{_bindir}/glava
%{_datadir}/glava


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.3-2
- Add xrandr dependency to fix FTBFS (#1733432)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.3-1
- Initial package of glava
