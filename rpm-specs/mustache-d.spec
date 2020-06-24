# This library only produces a static library, so there's no generated debuginfo
%global debug_package %{nil}

Name:           mustache-d
Version:        0.1.3
Release:        10%{?dist}
Summary:        Mustache template engine for D

License:        Boost
URL:            https://github.com/repeatedly/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Add license file referenced in the source code
# See https://github.com/repeatedly/mustache-d/issues/30
Source1:        http://www.boost.org/LICENSE_1_0.txt#/%{name}-LICENSE.txt

BuildRequires:  gcc
BuildRequires:  ldc
BuildRequires:  meson

ExclusiveArch:  %{ldc_arches}

%description
Mustache is a push-strategy (a.k.a logic-less) template engine.

This package provides the implementation for D.

%package devel
Summary:        Development files for using %{name}
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}

%description devel
Mustache is a push-strategy (a.k.a logic-less) template engine.

This package provides the development headers and static library
for integrating support for the Mustache template engine into
applications written in D.

%prep
%autosetup

# Fix version in meson.build
sed -i "s/project_version      = '.*'/project_version      = '%{version}'/" meson.build

# Rename license file
cp -a %{S:1} LICENSE

%build
export DFLAGS="%{_d_optflags}"
%meson
%meson_build

%install
%meson_install

%files devel
%doc README.markdown example/
%license LICENSE
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc
%{_d_includedir}/%{name}/


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Neal Gompa <ngompa13@gmail.com> - 0.1.3-7
- Add gcc BR to fix build in F29+ (rhbz#1604904)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 04 2018 Neal Gompa <ngompa13@gmail.com> - 0.1.3-5
- Rebuild against ldc 1.8.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Neal Gompa <ngompa13@gmail.com> - 0.1.3-1
- Initial packaging (#1433658)
