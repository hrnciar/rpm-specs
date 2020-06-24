
Name:           clazy
Summary:        Qt oriented code checker based on clang framework
Version:        1.6
Release:        3%{?dist}
License:        LGPLv2
URL:            https://cgit.kde.org/%{name}.git/
Source0:        https://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz

Patch0:         clazy-no-rpath.patch
# https://fedoraproject.org/wiki/Changes/Stop-Shipping-Individual-Component-Libraries-In-clang-lib-Package
Patch1:		0001-Link-against-libclang-cpp.so.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: clang-devel llvm-devel
BuildRequires: perl-podlators

Requires: clang

%description
clazy is a compiler plugin which allows clang to understand Qt semantics.
You get more than 50 Qt related compiler warnings, ranging from unneeded
memory allocations to misusage of API, including fix-its for automatic
refactoring.


%prep
%setup -q -n %{name}-%{version}

%patch0 -p1 -b .clazy-no-rpath
%patch1 -p1 -b .libclang-cpp

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%ldconfig_scriptlets

%files
%doc HOWTO
%license COPYING*
%{_bindir}/clazy
%{_bindir}/clazy-standalone
%dir %{_docdir}/clazy
%{_docdir}/clazy/*
%{_mandir}/man1/clazy.1.gz
%{_libdir}/ClazyPlugin.so
%{_datadir}/metainfo/org.kde.clazy.metainfo.xml


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Tom Stellard <tstellar@redhat.com> - 1.6-2
- Link against libclang-cpp.so
- https://fedoraproject.org/wiki/Changes/Stop-Shipping-Individual-Component-Libraries-In-clang-lib-Package

* Wed Oct 30 2019 Jan Grulich <jgrulich@redhat.com> - 1.6-1
- 1.6

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 30 2019 Tom Stellard <tstellar@redhat.com> - 1.5-2
- Rebuild for clang-8.0.0

* Sun Feb 03 2019 Jan Grulich <jgrulich@redhat.com> - 1.5-1
- Update to 1.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 03 2018 Jan Grulich <jgrulich@redhat.com> - 1.4-2
- Require clang

* Tue Oct 02 2018 Jan Grulich <jgrulich@redhat.com> - 1.4-1
- Initial version
