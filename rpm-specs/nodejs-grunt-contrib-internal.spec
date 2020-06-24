%{?nodejs_find_provides_and_requires}

Name:       nodejs-grunt-contrib-internal
Version:    0.4.13
Release:    9%{?dist}
Summary:    Internal tasks for managing the grunt-contrib project
License:    MIT
URL:        https://github.com/gruntjs/grunt-contrib-internal
Source0:    http://registry.npmjs.org/grunt-contrib-internal/-/grunt-contrib-internal-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%description
%{summary}.


%prep
%setup -q -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-contrib-internal
# CONTRIBUTING.md needs to be in libdir (RHBZ#1288025)
cp -pr package.json tasks/ CONTRIBUTING.md \
    %{buildroot}%{nodejs_sitelib}/grunt-contrib-internal

%nodejs_symlink_deps


%files
%doc CONTRIBUTING.md README.md
%license LICENSE-MIT
%{nodejs_sitelib}/grunt-contrib-internal


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Tom Hughes <tom@compton.nu> - 0.4.13-1
- Update to 0.4.13 upstream release
- Remove npm(read-package-json) fixdep

* Thu Dec 03 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.4.9-4
- Add CONTRIBUTING.md to libdir (RHBZ#1288025)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.9-1
- update to upstream release 0.4.9

* Thu Mar 13 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.8-1
- initial package
