%global gem_name json_pure

Summary: JSON Implementation for Ruby
Name: rubygem-%{gem_name}
Version: 1.8.1
Release: 13%{?dist}
# TODO: License should be probably updated.
# https://github.com/flori/json/issues/213
License: GPLv2 or Ruby
URL: http://flori.github.com/json
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(bigdecimal)
BuildRequires: rubygem(test-unit)
BuildArch: noarch

%package doc
Summary: Documentation for %{name}
Requires:%{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%description
This is a JSON implementation in pure Ruby.

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Remove json-java.gemspec to avoid JRuby dependency due to jruby shebang.
rm %{buildroot}%{gem_instdir}/json-java.gemspec

for file in `find %{buildroot}/%{gem_instdir} -type f -perm /a+x`; do
    [ -z "`head -n 1 $file | grep \"^#!/\"`" ] && chmod -v 644 $file
done
for file in `find %{buildroot}/%{gem_instdir} -type f ! -perm /a+x`; do
    [ ! -z "`head -n 1 $file | grep \"^#!/\"`" ] && chmod -v 755 $file
done

%check
pushd .%{gem_instdir}
JSON=pure ruby -e 'Dir.glob "./tests/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_libdir}/json/ext/.*
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/diagrams
%exclude %{gem_instdir}/ext
%exclude %{gem_instdir}/java
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/README-json-jruby.markdown
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/GPL
%doc %{gem_instdir}/COPYING-json-jruby
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/CHANGES
%doc %{gem_instdir}/VERSION
%doc %{gem_instdir}/TODO


%files doc
%{gem_instdir}/tests
%{gem_instdir}/data
%{gem_instdir}/tools
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%doc %{gem_docdir}
%{gem_instdir}/install.rb
%{gem_instdir}/json*.gemspec

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 14 2020 Vít Ondruch <vondruch@redhat.com> - 1.8.1-12
- Avoid unexpected JRuby dependency.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 24 2016 Vít Ondruch <vondruch@redhat.com> - 1.8.1-4
- Require rubygem(bigdecimal) to fix FTBFS.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jul 22 2014 Vít Ondruch <vondruch@redhat.com> - 1.8.1-1
- Update to json_pure 1.8.1.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Vít Ondruch <vondruch@redhat.com> - 1.6.3-7
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.6.3-4
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 12 2011 Michal Fojtik <mfojtik@redhat.com> - 1.6.3-2
- Rebuild after Koji outage

* Thu Dec 8 2011 Michal Fojtik <mfojtik@redhat.com> - 1.6.3-1
- Version bump

* Fri Jun 3 2011 Michal Fojtik <mfojtik@redhat.com> - 1.5.1-1
- Version bump
- Removed gtk dependency to keep this lightweight

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 04 2010 Michal Fojtik <mfojtik@redhat.com> - 1.4.6-3
- Removed tests which was failing under F14

* Sat Oct 02 2010 Michal Fojtik <mfojtik@redhat.com> - 1.4.6-2
- Fixed failing test
- Removed unusefull rm call

* Mon Aug 02 2010 Michal Fojtik <mfojtik@redhat.com> - 1.4.6-1
- Version bump
- Removed BuildRoot
- Moved 'rm' from check to install
- Moved files from -doc to main package and install.rb to -doc

* Tue Jul 20 2010 Michal Fojtik <mfojtik@redhat.com> - 1.4.3-1
- Initial package
