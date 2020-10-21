%global gem_name gherkin

Name: rubygem-%{gem_name}
Version: 5.1.0
Release: 5%{?dist}
Summary: Fast Gherkin lexer/parser
License: MIT
URL: https://github.com/cucumber/gherkin-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/cucumber/gherkin-ruby && cd gherkin-ruby
# git checkout v5.1.0 && tar czvf rubygem-gherkin-5.1.0-make.tar.gz Makefile testdata/ bin/gherkin-generate-tokens
Source1: %{name}-%{version}-make.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: %{_bindir}/jq
BuildArch: noarch

%description
A fast Gherkin lexer/parser based on the Ragel State Machine Compiler.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.


%prep
%setup -q -n %{gem_name}-%{version} -b 1

%build
# Create the gem as gem install only works -on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
find %{buildroot}%{gem_instdir}/bin -type f | \
  xargs sed -i 's|^#!/usr/bin/env ruby$|#!/usr/bin/ruby|'

%check
pushd .%{gem_instdir}

rspec spec

# Files needed for make to pass.
ln -s %{_builddir}/Makefile ./Makefile
ln -s %{_builddir}/testdata ./testdata
ln -s %{_builddir}/bin/gherkin-generate-tokens ./bin/gherkin-generate-tokens

sed -i '/.built:/ i .built:\n' Makefile
sed -i '/.built: /,/^$/ s/^/#/' Makefile

make .compared
popd

%files
%dir %{gem_instdir}
%{_bindir}/gherkin-ruby
%{_bindir}/gherkin
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/spec

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 03 2018 Jaroslav Prokop <jar.prokop@volny.cz> - 5.1.0-1
- Update to Gherkin 5.1.0.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jun Aruga <jaruga@redhat.com> - 4.1.3-1
- Update to Gherkin 4.1.3.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Jun Aruga <jaruga@redhat.com> - 4.0.0-1
- Update to Gherkin 4.0.0.

* Tue Mar 01 2016 Vít Ondruch <vondruch@redhat.com> - 3.2.0-1
- Update to Gherkin 3.2.0.

* Tue Mar 01 2016 Vít Ondruch <vondruch@redhat.com> - 2.12.2-8
- Cleanup the .spec and enable the test suite.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.12.2-6
- F-24: rebuild against ruby23
- Bootstrap, once disable test

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.12.2-4
- Enable test suite again

* Thu Jan 15 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.12.2-3
- Rebuild for ruby 2.2
- Bootstrap, once disable test

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Josef Stribny <jstribny@redhat.com> - 2.12.2-1
- Update to gherkin 2.12.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Vít Ondruch <vondruch@redhat.com> - 2.11.6-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Tue Aug  6 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.11.6-5
- Again enable test suite

* Tue Aug  6 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.11.6-4
- Bootstrap

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 20 2013 Vít Ondruch <vondruch@redhat.com> - 2.11.6-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Add bootstrap code.

* Mon Feb 18 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 2.11.6-1
- Updated to version 2.11.6.
- Fixed wrong dates in changelog.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Mar 29 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.9.3-1
- Update to 2.9.3
- Introduced %%check section

* Mon Jan 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.4.5-4
- Removed *.so files from %%{gem_libdir}.

* Mon Jan 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.4.5-3
- Rebuilt for Ruby 1.9.3.
- Significantly simplified build process.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 12 2011 Mo Morsi <mmorsi@redhat.com> - 2.4.5-1
- Update to latest upstream release

* Wed Jun 08 2011 Chris Lalancette <clalance@redhat.com> - 2.3.3-3
- Significantly revamped spec to conform more to fedora standards
- Fix build on Rawhide

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Michal Fojtik <mfojtik@redhat.com> - 2.3.3-1
- Version bump

* Fri Sep 24 2010 Michal Fojtik <mfojtik@redhat.com> - 2.2.4-3
- Replaced ~> with >= in JSON version so now it can be used
  with latest json as well

* Fri Sep 24 2010 Michal Fojtik <mfojtik@redhat.com> - 2.2.4-2
- Fixed JSON dependency version

* Fri Sep 24 2010 Michal Fojtik <mfojtik@redhat.com> - 2.2.4-1
- Version bump

* Wed Sep 08 2010 Michal Fojtik <mfojtik@redhat.com> - 2.2.0-1
- Version bump

* Tue Jul 20 2010 Michal Fojtik <mfojtik@redhat.com> - 2.1.5-3
- Fixed rspec and trollop versions in gemspec files

* Tue Jul 20 2010 Michal Fojtik <mfojtik@redhat.com> - 2.1.5-2
- Added -doc subpackage
- Fixed debugging symbols issue (Thanks mtasaka)
- Fixed path for pushd in install section
- Fixed trollop version in gemspec
- Removed '#line foo' from C files

* Mon Jul 19 2010 Michal Fojtik <mfojtik@redhat.com> - 2.1.5-1
- Updated to latest version
- Fixed compiler flags
- Fixed directory ownership
- Removed unwanted versioning files
- Placed .so files on right place

* Wed Jul 14 2010 Michal Fojtik <mfojtik@redhat.com> - 2.1.3-1
- Initial package
