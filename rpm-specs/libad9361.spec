%global git_commit_0 6027674bc2ef400147f1607d0252e5347163f2f7
%global git_snap_date 20170207

%global git_user analogdevicesinc
%global git_project libad9361-iio

%global git_short_commit_0 %(c=%{git_commit_0}; echo ${c:0:7})

Name:          libad9361
Version:       0
Release:       0.7.%{git_snap_date}git%{git_short_commit_0}%{?dist}
Summary:       Library for access to Analog Devices AD9361 radio IC

License:       LGPLv2+

URL:           https://github.com/%{git_user}/%{git_project}/

#Source0:       https://github.com/%{git_user}/%{git_project}/archive/v%{version}/%{name}-%{version}.tar.gz
Source0:        https://github.com/%{git_user}/%{git_project}/archive/%{git_commit_0}/%{name}-%{git_short_commit_0}.tar.gz

BuildRequires: gcc
BuildRequires: cmake
BuildRequires: pkgconfig(libiio)


%description
Library for access to Analog Devices AD9361 radio IC.


%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.


%prep
%setup -q -n %{git_project}-%{git_commit_0}

%build
if [ "%{_libdir}" = "%{_prefix}/lib64" ]; then
  %cmake -DINSTALL_LIB_DIR=%{_libdir} .
else
  %cmake .
fi

%make_build V=1

%install
%make_install INSTALL='install -p'

# Remove libtool archives.
find %{buildroot} -name '*.la' -delete

%ldconfig_scriptlets


%files
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/ad9361.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.20170207git6027674
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20170207git6027674
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20170207git6027674
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20170207git6027674
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20170207git6027674
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 19 2017 Eric Smith <brouhaha@fedoraproject.org> 0-0.2.20170207git6027674
- Update per package review (#1482246) comments.

* Wed Aug 16 2017 Eric Smith <brouhaha@fedoraproject.org> 0-0.1.20170207git6027674
- Initial version.
