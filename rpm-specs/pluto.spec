%global commit c6cab36140648828ccc72cc659d55d274508da0d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           pluto
Version:        0
Release:        0.11git%{shortcommit}%{?dist}
Summary:        Small utility library for SHA1, Tiny Encryption Algorithm, and UUID4

License:        GPLv3+
URL:            https://gitlab.com/CollectiveTyranny/pluto
Source0:        %{url}/repository/archive.tar.gz?ref=%{commit}#/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make

%description
%{summary}.

%package devel
Summary:        Development files and headers for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%package doc
Summary:        Documentation for %{name}-devel
BuildRequires:  doxygen
BuildArch:      noarch

%description doc
%{summary}.

%prep
%autosetup -n %{name}-%{commit}-%{commit}
mkdir %{_target_platform}

%build
pushd %{_target_platform}
  %cmake ..
popd
%make_build -C %{_target_platform}
%make_build doc -C %{_target_platform}

%install
%make_install -C %{_target_platform}

%ldconfig_scriptlets

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so

%files doc
%license LICENSE
%doc doc/html

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11gitc6cab36
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2gitc6cab36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 27 2016 Igor Gnatenko <ignatenko@redhat.com> - 0-0.1gitc6cab36
- Initial package
