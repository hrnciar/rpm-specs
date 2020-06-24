%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-through
Version:        2.3.8
Release:        8%{?dist}
Summary:        Simplified stream construction for Node.js
License:        MIT or ASL 2.0
URL:            https://github.com/dominictarr/through
Source0:        http://registry.npmjs.org/through/-/through-%{version}.tgz
BuildArch:      noarch

%if 0%{?fedora} >= 19
ExclusiveArch:  %{nodejs_arches} noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(tape)
BuildRequires:  npm(from)
#BuildRequires:  npm(stream-spec)
%endif

%description
%{summary}.


%prep
%setup -q -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/through
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/through

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%__nodejs -e "require('./')"
%if 0%{?enable_tests}
# requires npm(stream-spec)
rm test/index.js
tape test/*.js
%endif


%files
%doc readme.markdown
%license LICENSE.APACHE2 LICENSE.MIT
%{nodejs_sitelib}/through


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Mar  7 2016 Tom Hughes <tom@compton.nu> - 2.3.8-1
- Update to 2.3.8 upstream release
- Enable as many tests as possible

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jul 30 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.3.4-2
- restrict to compatible arches

* Mon May 27 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.3.4-1
- initial package
