# ava not yet packaged
%global enable_tests 0
%global srcname path-exists

Epoch:          1
Name:           nodejs-%{srcname}
Version:        4.0.0
Release:        3%{?dist}
Summary:        Check if a path exists
License:        MIT
URL:            https://github.com/sindresorhus/path-exists
Source0:        https://registry.npmjs.com/%{srcname}/-/%{srcname}-%{version}.tgz
# Test file not in npm tarball
Source1:        https://raw.githubusercontent.com/sindresorhus/%{srcname}/v%{version}/test.js

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(ava)
BuildRequires:  npm(tsd)
BuildRequires:  npm(xo)
%endif

%description
%{summary}.

%prep
%autosetup -n package
cp -p %{SOURCE1} .

%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{srcname}
cp -pr index.js package.json \
    %{buildroot}%{nodejs_sitelib}/%{srcname}

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
ava
%endif


%files
%doc readme.md
%license license
%{nodejs_sitelib}/%{srcname}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Jan Staněk <jstanek@redhat.com> - 1:4.0.0-1
- Update to version 4.0.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 22 2017 Jared Smith <jsmith@fedoraproject.org> - 1:3.0.0-1
- Update to upstream 3.0.0 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 13 2015 Piotr Popieluch <piotr1212@gmail.com> - 1:2.1.0-1
- Update to 2.1.0
- Bump epoch, version 2.0.0 was pushed with version tag: 2.2.0

* Sat Oct 17 2015 Piotr Popieluch <piotr1212@gmail.com> - 2.0.0-1
- Initial package
