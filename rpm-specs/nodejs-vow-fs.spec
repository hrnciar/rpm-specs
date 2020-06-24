# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:               nodejs-vow-fs
Version:            0.3.6
Release:            2%{?dist}
Summary:            File I/O by Vow

# https://github.com/dfilatov/vow-fs/blob/master/lib/fs.js
License:            MIT and GPLv3
URL:                https://www.npmjs.org/package/vow-fs
Source0:            https://github.com/dfilatov/vow-fs/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:          noarch
ExclusiveArch:      %{nodejs_arches} noarch

BuildRequires:      nodejs-packaging >= 6

%if 0%{?enable_tests}
BuildRequires:      npm(nodeunit)
BuildRequires:      npm(glob)
BuildRequires:      npm(uuid)
BuildRequires:      npm(vow)
BuildRequires:      npm(vow-queue)
%endif


%description
[Vow](https://github.com/dfilatov/vow)-based file I/O for Node.js

%prep
%autosetup -n vow-fs-%{version}
%nodejs_fixdep glob "^6.0.3"
%nodejs_fixdep node-uuid "^1.4.1"
rm -rf node_modules/


%build
%nodejs_symlink_deps --build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/vow-fs
cp -pr package.json lib \
    %{buildroot}%{nodejs_sitelib}/vow-fs
%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
%__nodejs test/runner.js
%endif


%files
%doc README.md
%{nodejs_sitelib}/vow-fs/


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Jared K. Smith <jsmith@fedoraproject.org> - 0.3.6-1
- Update to upstream 0.3.6 release

* Tue Oct 08 2019 Jared Smith - 0.3.4-9
- Remove unneeded dependency on npm(istanbul)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 0.3.4-1
- Update to 0.3.4 upstream release
- Enable tests

* Mon Jul 13 2015 Parag Nemade <pnemade AT fedoraproject DOT org> - 0.3.2-4
- fixdep npm(vow-queue)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jul 21 2014 Ralph Bean <rbean@redhat.com> - 0.3.2-2
- Specified noarch.

* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 0.3.2-1
- Initial packaging for Fedora.
