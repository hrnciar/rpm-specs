# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global npm_name handlebars

Name:		nodejs-%{npm_name}
Version:	4.0.13
Release:	3%{?dist}
Summary:	Mustache extension for Node.js

License:	MIT
URL:		  http://handlebarsjs.com/
Source0:	https://registry.npmjs.org/handlebars/-/%{npm_name}-%{version}.tgz

Requires:	npm(uglify-js)
Requires:	npm(optimist)

BuildRequires:	npm(uglify-js)
BuildRequires:	npm(optimist)
BuildRequires:	nodejs-devel
BuildRequires:	nodejs-packaging

BuildArch:	noarch

%if 0%{?rhel} && 0%{?rhel} < 7
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch
%else
ExclusiveArch:	%{nodejs_arches} noarch
%endif

%description
Handlebars.js is an extension to the Mustache templating language created by
Chris Wanstrath. Handlebars.js and Mustache are both logicless templating
languages that keep the view and the code separated like we all know they should
be.

%prep
%setup -q -n package

# Remove bundled optimist
rm -rf node_modules

%nodejs_fixdep optimist '0.x'
%nodejs_fixdep source-map '^0.5.2'
%nodejs_fixdep async

%build
# nothing to build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{nodejs_sitelib}/handlebars
chmod a+x bin/handlebars
cp -rp bin dist package.json lib runtime.js %{buildroot}/%{nodejs_sitelib}/handlebars

# Install /usr/bin/handlebars
ln -s %{nodejs_sitelib}/handlebars/bin/handlebars \
      %{buildroot}%{_bindir}

%nodejs_symlink_deps

%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
grunt
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.markdown release-notes.md
%{nodejs_sitelib}/handlebars/
%{_bindir}/handlebars


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Parag Nemade <pnemade@redhat.com> - 4.0.13-1
- Update to 4.0.13 version (rh#1685825)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 21 2017 Parag Nemade <pnemade AT redhat DOT com> - 4.0.11-1
- Update to 4.0.11 version (#1504365)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 21 2017 Parag Nemade <pnemade AT redhat DOT com> - 4.0.10-1
- Update to 4.0.10 version

* Wed May 03 2017 Parag Nemade <pnemade AT redhat DOT com> - 4.0.8-1
- Update to 4.0.8 version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 21 2016 Parag Nemade <pnemade AT redhat DOT com> - 4.0.6-1
- Update to 4.0.6

* Wed Feb 10 2016 Tom Hughes <tom@compton.nu> - 4.0.5-3%{dist}
- Update npm(source-map) dependency

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 20 2015 Piotr Popieluch <piotr1212@gmail.com> - 4.0.5-1
- Update to 4.0.5

* Sat Oct 17 2015 Piotr Popieluch <piotr1212@gmail.com> - 4.0.3-1
- Update to 4.0.3

* Mon Aug 24 2015 Piotr Popieluch <piotr1212@gmail.com> - 3.0.3-3
- Set correct el6 architecture
- Update url to use https

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 24 2015 Piotr Popieluch <piotr1212@gmail.com> - 3.0.3-1
- Update to 3.0.3
- Fixdep optimist and source-map
- Removed deprecated Group: tag
- Removed symlinkdep from build section

* Sat Apr 04 2015 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1

* Wed Dec 10 2014 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 2.0.0-4
- Fixing lib directory install (#1172471)

* Mon Dec 08 2014 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 2.0.0-3
- Adding dist directory (#1171403)

* Tue Nov 25 2014 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 2.0.0-2
- Fixing symlink to CLI

* Thu Nov 20 2014 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 2.0.0-1
- Update to final release 2.0.0
- Adding missing Requires

* Fri Jul 25 2014 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 2.0.0-0.1.alpha.4
- Initial packaging
