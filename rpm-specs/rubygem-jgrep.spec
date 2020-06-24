%global gem_name jgrep

Name:           rubygem-%{gem_name}
Version:        1.5.1
Release:        2%{?dist}
Summary:        Filter JSON documents with a simple logical language

License:        ASL 2.0
URL:            http://jgrep.org/
Source0:        https://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildArch:      noarch

BuildRequires:  rubygems-devel
%if 0%{?rhel} == 0
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(mocha)
%endif
Requires:       ruby(release) >= 1.8
Requires:       rubygems
Provides:       rubygem(%{gem_name}) = %{version}-%{release}

# Drag in the pure Ruby implementation too, so that jruby has something to
# fall back to: https://bugzilla.redhat.com/show_bug.cgi?id=1219502
Requires:       rubygem(json_pure)

%description
JGrep is  Ruby-based CLI tool and API for parsing and displaying JSON data
using a logical expression syntax. It allows you to search a list of JSON
documents and return specific documents or values based on logical truths.


%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for %{name}


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{_bindir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
cp -a ./%{_bindir}/* %{buildroot}%{_bindir}


%if 0%{?rhel} == 0
%check
rspec -Ilib spec
%endif


%files
%{_bindir}/*
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/*.markdown
%exclude %{gem_instdir}/COPYING
%{gem_spec}
%doc CHANGELOG.markdown README.markdown
%license COPYING


%files doc
%{gem_docdir}
%{gem_instdir}/Rakefile
%{gem_instdir}/spec


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Steve Traylen <steve.traylen@cern.ch> - 1.5.1-1
- Update to 1.5.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 03 2017 Steve Traylen <steve.traylen@cern.ch> - 1.5.0-1
- Update to 1.5.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 21 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.4.1-1
- Update to 1.4.1

* Tue Mar 01 2016 Dominic Cleal <dcleal@redhat.com> - 1.4.0-1
- Update to 1.4.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May  7 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.3.3-5
- Work around JRuby woes (rh #1219502)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Lubomir Rintel <lkundrak@v3.sk> - 1.3.3-3
- Disable tests on rhel

* Tue Apr 29 2014 Lubomir Rintel <lkundrak@v3.sk> - 1.3.3-2
- Run tests (Lukas Bezdicka, #1092000)
- Fix issue with tests. (Guess adding the run was a good idea...)

* Mon Apr 28 2014 Lubomir Rintel <lkundrak@v3.sk> - 1.3.3-1
- Initial packaging
