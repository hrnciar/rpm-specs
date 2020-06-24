%global gem_name sqlite3

Name: rubygem-%{gem_name}
Version: 1.4.2
Release: 2%{?dist}
Summary: Allows Ruby scripts to interface with a SQLite3 database
License: BSD
URL: https://github.com/sparklemotion/sqlite3-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: sqlite-devel
BuildRequires: rubygem(minitest) >= 5.0.0
BuildRequires: gcc

%description
SQLite3/Ruby is a module to allow Ruby scripts to interface with a SQLite3
database.

%package doc
Summary: Documentation for %{name}
License: BSD and LGPLv2
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,sqlite3} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
pushd .%{gem_instdir}
ruby -I$(dirs +1)%{gem_extdir_mri}:lib:test -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/API_CHANGES.rdoc
%doc %{gem_instdir}/CHANGELOG.rdoc
%doc %{gem_instdir}/ChangeLog.cvs
%doc %{gem_instdir}/Manifest.txt
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/appveyor.yml
%doc %{gem_instdir}/faq
%{gem_instdir}/rakelib
%{gem_instdir}/setup.rb
%{gem_instdir}/test

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.2-1
- Update to 1.4.2 (to make test pass for ruby 27)
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Vít Ondruch <vondruch@redhat.com> - 1.4.1-1
- Update to sqlite3 1.4.1.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Vít Ondruch <vondruch@redhat.com> - 1.3.13-10
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Fri Jul 27 2018 Vít Ondruch <vondruch@redhat.com> - 1.3.13-9
- Add "BR: gcc" to fix FTBFS (rhbz#1606268).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.3.13-7
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.13-6
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Vít Ondruch <vondruch@redhat.com> - 1.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Thu Jan 05 2017 Vít Ondruch <vondruch@redhat.com> - 1.3.13-1
- Update to sqlite3 1.3.13.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 07 2016 Vít Ondruch <vondruch@redhat.com> - 1.3.11-1
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3
- Update to sqlite3 1.3.11.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Vít Ondruch <vondruch@redhat.com> - 1.3.10-1
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2
- Update to sqlite3 1.3.10.

* Tue Oct 07 2014 Josef Stribny <jstribny@redhat.com> - 1.3.9-3
- Fix: Big Endian for Power

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Josef Stribny <jstribny@redhat.com> - 1.3.9-1
- Update to sqlite3 1.3.9

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 10 2014 Josef Stribny <jstribny@redhat.com> - 1.3.8-1
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1
- Update to 1.3.8

* Wed Nov 27 2013 Vít Ondruch <vondruch@redhat.com> - 1.3.7-3
- Prevent dangling symlink in -debuginfo.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 03 2013 Vít Ondruch <vondruch@redhat.com> - 1.3.7-1
- Update to sqlite3 1.3.7.
- Fix -doc license (rhbz#969963).

* Thu Feb 28 2013 Vít Ondruch <vondruch@redhat.com> - 1.3.5-4
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 02 2012 Vít Ondruch <vondruch@redhat.com> - 1.3.5-1
- Updated to sqlite3 1.3.5.

* Thu Jan 19 2012 Vít Ondruch <vondruch@redhat.com> - 1.3.4-3
- Rebuilt for Ruby 1.9.3.
- Drop ruby-sqlite3 subpackage.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 20 2011 Vít Ondruch <vondruch@redhat.com> - 1.3.4-1
- Updated to sqlite3 1.3.4.
- Use the upstream big endian fix.

* Wed Jun 22 2011 Dan Horák <dan[at]danny.cz> - 1.3.3-5
- fix build on big endian arches (patch by Vít Ondruch)

* Fri Jun 03 2011 Vít Ondruch <vondruch@redhat.com> - 1.3.3-4
- The subdirectory of ruby_sitearch has to be owned by package.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Feb 03 2011 Vít Ondruch <vondruch@redhat.com> - 1.3.3-2
- Updated links.
- Removed obsolete BuildRoot.
- Removed unnecessary cleanup.

* Wed Feb 02 2011 Vít Ondruch <vondruch@redhat.com> - 1.3.3-1
- Package renamed from rubygem-sqlite3-ruby to rubygem-sqlite3.
- Test suite executed upon build.
- Documentation moved into separate package.
- Removed clean section which is not necessary.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.4-4
- F-12: Rebuild to create valid debuginfo rpm again (ref: #505774)

* Tue Jun 16 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.4-3
- Create ruby-sqlite3 as subpackage (ref: #472621, #472622)
- Use gem as source

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 13 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.2.4-1
- Fix items from review (#459881)
- New upstream version

* Sun Aug 31 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.2.2-2
- Fix items from review (#459881)

* Sun Jul 13 2008 Matt Hicks <mhicks@localhost.localdomain> - 1.2.2-1
- Initial package
