%global gem_name bcrypt

Name: rubygem-%{gem_name}
Version: 3.1.12
Release: 8%{?dist}
Summary: Wrapper around bcrypt() password hashing algorithm
# ext/* - Public Domain
# spec/TestBCrypt.java - ISC
License: MIT and Public Domain and ISC
URL: https://github.com/codahale/bcrypt-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: rubygem(rspec)
BuildRequires: gcc
# bcrypt-ruby is renamed to brypt
Provides: rubygem(brypt-ruby) = %{version}
Provides: rubygem-bcrypt-ruby = %{version}-%{release}
Obsoletes: rubygem-bcrypt-ruby <= 3.1.2-2

%description
bcrypt() is a sophisticated and secure hash algorithm designed by The
OpenBSD project for hashing passwords. bcrypt-ruby provides a simple,
humane wrapper for safely handling passwords.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

%build
# noop

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
pushd .%{gem_instdir}
rspec -I$(dirs +1)%{gem_extdir_mri} spec
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/appveyor.yml
%license %{gem_instdir}/COPYING
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG
%{gem_instdir}/Gemfile*
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/spec

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Vít Ondruch <vondruch@redhat.com> - 3.1.12-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Vít Ondruch <vondruch@redhat.com> - 3.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Björn Esser <besser82@fedoraproject.org> - 3.1.12-1
- Update to BCrypt 3.1.12. (#1579089)

* Wed Apr 25 2018 Björn Esser <besser82@fedoraproject.org> - 3.1.11-9
- Update patch for libxcrypt

* Fri Feb 16 2018 Björn Esser <besser82@fedoraproject.org> - 3.1.11-8
- Add patch to build against libxcrypt (#1537140)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 3.1.11-6
- Rebuilt for switch to libxcrypt

* Wed Jan 03 2018 Vít Ondruch <vondruch@redhat.com> - 3.1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.5

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Vít Ondruch <vondruch@redhat.com> - 3.1.11-1
- Update to BCrypt 3.1.11.

* Tue Jan 10 2017 Vít Ondruch <vondruch@redhat.com> - 3.1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Vít Ondruch <vondruch@redhat.com> - 3.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Josef Stribny <jstribny@redhat.com> - 3.1.10-1
- Update to 3.1.10

* Thu Jan 15 2015 Vít Ondruch <vondruch@redhat.com> - 3.1.9-1
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2
- Update to BCrypt 3.1.9.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Josef Stribny <jstribny@redhat.com> - 3.1.7-5
- Fix provides to reflect rubygem(brypt-ruby) as well

* Thu Apr 10 2014 Josef Stribny <jstribny@redhat.com> - 3.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Mon Apr 07 2014 Josef Stribny <jstribny@redhat.com> - 3.1.7-3
- Fix typo, obsoletes, upstream URL

* Thu Mar 20 2014 Josef Stribny <jstribny@redhat.com> - 3.1.7-2
- Create -doc subpackage
- Fix obsoletes

* Tue Mar 18 2014 Josef Stribny <jstribny@redhat.com> - 3.1.7-1
- Rename package to rubygem-bcrypt (this obsoletes bcrypt-ruby)
- Update to bcrypt 3.1.7

* Wed Nov 27 2013 Vít Ondruch <vondruch@redhat.com> - 3.1.2-2
- Prevent dangling symlink in -debuginfo.

* Mon Nov 11 2013 Josef Stribny <jstribny@redhat.com> - 3.1.2-1
- Update to brypt-ruby 3.1.2

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 01 2013 Vít Ondruch <vondruch@redhat.com> - 3.0.1-7
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 02 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.1-4
- Fixed wrong provide.

* Mon Jan 23 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.1-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 14 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.1-1
- Update to bcrypt-ruby 3.0.1.

* Mon Aug 08 2011 Mo Morsi <mmorsi@redhat.com> - 2.1.2-4
- Replace BR(check) with BR

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 24 2010 Mohammed Morsi <mmorsi@redhat.com> - 2.1.2-2
- Updates / fixes based on review feedback
- Fixed bcrypt_ext.so install location

* Tue Aug 10 2010 Mohammed Morsi <mmorsi@redhat.com> - 2.1.2-1
- Initial package
