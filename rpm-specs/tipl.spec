%global commit 6a5938047287eb90b63f441f3e5dd67fb5581408
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           tipl
Version:        0
Release:        0.9.git%{shortcommit}%{?dist}
Summary:        Template image processing library

License:        BSD
URL:            https://github.com/frankyeh/TIPL
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# https://github.com/frankyeh/TIPL/pull/4
Patch0001:      0001-add-CMake-build-definitions-and-pkgconfig-file.patch
Patch0002:      0002-unbundle-SVM.patch

BuildRequires:  cmake
BuildRequires:  make
BuildArch:      noarch

%description
%{summary}.

%package        devel
Summary:        %{summary}
Requires:       libsvm-devel

%description    devel
Header-only template image processing library.

%prep
%autosetup -n TIPL-%{commit} -p1
mkdir %{_target_platform}

%build
pushd %{_target_platform}
  %cmake ..
popd
%make_build -C %{_target_platform}

%install
%make_install -C %{_target_platform}

%files devel
%license COPYRIGHT
%doc README.md
%{_includedir}/image.hpp
%{_includedir}/image/
%{_datadir}/pkgconfig/%{name}.pc

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git6a59380
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git6a59380
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git6a59380
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git6a59380
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git6a59380
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git6a59380
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git6a59380
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Aug 13 2016 Igor Gnatenko <ignatenko@redhat.com> - 0-0.2.git6a59380
- Update to latest snapshot

* Sat Dec 12 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0-0.1.git5ffc80c
- Initial package
