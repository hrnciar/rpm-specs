%global user    gabime

Name:           spdlog
Version:        1.6.1
Release:        1%{?dist}
Summary:        Super fast C++ logging library
License:        MIT
URL:            https://github.com/%{user}/%{name}
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  google-benchmark-devel
BuildRequires:  fmt-devel >= 6.1.2
BuildRequires:  ninja-build
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  gcc

%description
This is a packaged version of the gabime/spdlog C++ logging
library available at Github.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       libstdc++-devel%{?_isa}
Requires:       fmt-devel%{?_isa}

%description devel
The %{name}-devel package contains C++ header files for developing
applications that use %{name}.

%prep
%autosetup -p1
mkdir -p %{_target_platform}
find . -name '.gitignore' -exec rm {} \;
sed -i -e "s,\r,," README.md

%build
pushd %{_target_platform}
    %cmake -G Ninja \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DCMAKE_BUILD_TYPE=Release \
    -DSPDLOG_BUILD_SHARED=ON \
    -DSPDLOG_BUILD_EXAMPLE=OFF \
    -DSPDLOG_BUILD_BENCH=OFF \
    -DSPDLOG_BUILD_TESTS=ON \
    -DSPDLOG_INSTALL=ON \
    -DSPDLOG_FMT_EXTERNAL=ON \
    ..
popd
%ninja_build -C %{_target_platform}

%check
pushd %{_target_platform}
    ctest --output-on-failure
popd

%install
%ninja_install -C %{_target_platform}

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.1*

%files devel
%doc example
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue Jun 02 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.6.1-1
- Updated to version 1.6.1.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.5.0-1
- Updated to version 1.5.0.

* Wed Dec 18 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.4.2-1
- Updated to version 1.4.2.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 20 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.3.1-1
- Updated to version 1.3.1.

* Mon Nov 05 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.1-1
- Updated to version 1.2.1.

* Sun Sep 02 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1.0-1
- Updated to version 1.1.0.

* Thu Aug 09 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.0-1
- Updated to version 1.0.0.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.17.0-1
- Updated to version 0.17.0.
- Added tests support.
- Added cmake and pkg-config support.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Sep 04 2016 Daniel Kopecek <dkopecek@redhat.com> - 0.10.0-1
- Update to 0.10.0

* Fri Jul 08 2016 Daniel Kopecek <dkopecek@redhat.com> - 0-8.20160703git34bb86b
- update to rev 34bb86b

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-7.20151110gitcbc8ba7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Daniel Kopecek <dkopecek@redhat.com> - 0-6.20151110gitcbc8ba7
- update to rev cbc8ba7

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-5.20150410git211ce99
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Daniel Kopecek <dkopecek@redhat.com> - 0-4.20150410git211ce99
- don't build the base package
- remove a dot from the release tag
- corrected -devel subpackage description

* Mon Apr 20 2015 Daniel Kopecek <dkopecek@redhat.com> - 0-3.20150410git.211ce99
- use the -p option when copying the header files

* Tue Apr 14 2015 Daniel Kopecek <dkopecek@redhat.com> - 0-2.20150410git.211ce99
- don't build the debuginfo subpackage
- require libstdc++-devel
- don't generate a distribution specific pkg-config file

* Fri Apr 10 2015 Daniel Kopecek <dkopecek@redhat.com> - 0-1.20150410git.211ce99
- Initial package
