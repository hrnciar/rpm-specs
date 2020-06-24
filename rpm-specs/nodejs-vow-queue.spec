# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename vow-queue

Name:               nodejs-vow-queue
Version:            0.4.1
Release:            10%{?dist}
Summary:            Vow-based task queue

License:            MIT and GPLv3+
URL:                https://www.npmjs.org/package/vow-queue
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
BuildArch:          noarch

%if 0%{?fedora} >= 19
ExclusiveArch:      %{nodejs_arches} noarch
%else
ExclusiveArch:      %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:      nodejs-packaging >= 6

BuildRequires:      npm(vow)

Requires:           npm(vow)

%if 0%{?enable_tests}
BuildRequires:      npm(jscs)
BuildRequires:      npm(vow)
BuildRequires:      npm(jshint)
BuildRequires:      npm(istanbul)
BuildRequires:      npm(mocha-istanbul)
BuildRequires:      npm(chai)
BuildRequires:      npm(mocha)
%endif


%description
vow-queue is a module for task queue with weights and priorities

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/vow-queue
cp -pr package.json lib \
    %{buildroot}%{nodejs_sitelib}/vow-queue

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
make validate
%endif


%files
%doc CHANGELOG.md README.md LICENSE
%{nodejs_sitelib}/vow-queue/

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 14 2015 Ralph Bean <rbean@redhat.com> - 0.4.1-1
- new version

* Mon Jul 21 2014 Ralph Bean <rbean@redhat.com> - 0.3.1-2
- Completed license field.
- Specified noarch.

* Tue Jul 08 2014 Ralph Bean <rbean@redhat.com> - 0.3.1-1
- Initial packaging for Fedora.
