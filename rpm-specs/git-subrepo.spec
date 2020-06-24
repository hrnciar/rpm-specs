Name: git-subrepo
Version: 0.4.0
Release: 4%{?dist}

License: MIT
Summary: Git Submodule Alternative
URL: https://github.com/ingydotnet/%{name}
BuildArch: noarch

Source0: %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: %{name}-fix-shebangs.patch

Requires: git-core
BuildRequires: git

%description
This git command "clones" an external git repo into a subdirectory
of your repo. Later on, upstream changes can be pulled in, and local
changes can be pushed back. Simple.

%prep
%autosetup -p1

%build
# Nothing to build...

%install
%make_install PREFIX=%{_prefix}

%files
%license License
%doc ReadMe.pod Intro.pod Changes
%{_libexecdir}/git-core/%{name}
%{_libexecdir}/git-core/%{name}.d
%{_mandir}/man1/*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.0-1
- Updated to version 0.4.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2.20170206gita7ee886
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.1-1.20170206gita7ee886
- Initial release.
