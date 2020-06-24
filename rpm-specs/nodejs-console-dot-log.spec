%{?nodejs_find_provides_and_requires}

Name:       nodejs-console-dot-log
Version:    0.1.3
Release:    15%{?dist}
Summary:    A console.log implementation that plays nice with large amounts of data
# License is specified in console.log.js.
# Upstream have been informed about missing LICENSE file:
# https://gist.github.com/tmpvar/1077544#comment-770148
License:    MIT
URL:        https://gist.github.com/1077544
Source0:    http://registry.npmjs.org/console.log/-/console.log-%{version}.tgz
# Include a copy of the MIT license to comply with license requirements.
Source20:   LICENSE

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%description
A console.log implementation that plays nice with large amounts of data.
It keeps the node alive until the output has flushed to the screen.


%prep
%setup -q -n package
cp -a %{SOURCE20} .


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/console.log
cp -pr package.json console.log.js \
    %{buildroot}%{nodejs_sitelib}/console.log

%nodejs_symlink_deps


%files
%doc LICENSE README.md
%{nodejs_sitelib}/console.log


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 06 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.3-4
- fix compatible arches for f18/el6

* Fri Jul 05 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.3-3
- restrict to compatible arches

* Fri Jun 07 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.3-2
- rename from nodejs-console-log to nodejs-console-dot-log, as the real npm
  registry name of this module is "console.log" and there is already another
  npm module called "console-log"

* Sun Feb 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.3-1
- initial package
