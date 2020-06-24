
%global gem_name ruby-ldap

# Package should be named rubygem-ruby-ldap
# Fix at a later stage.
Name:           %{gem_name}
Version:        0.9.16
Release:        19%{?dist}
Summary:        Ruby LDAP libraries
License:        BSD 
URL:            http://ruby-ldap.sourceforge.net/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires: openldap-devel 
BuildRequires: openssl-devel 
BuildRequires: ruby(release)
BuildRequires: rubygems-devel 
BuildRequires: ruby-devel 
BuildRequires: gcc
BuildRequires: rubygem(did_you_mean)

%if 0%{?fc20} || 0%{?el7}
Requires: ruby(release)
Requires: ruby(rubygems)
%endif

# Historical should be removed.
Provides:       ruby(ldap) = %{version}-%{release}

%if 0%{?fc20} || 0%{?el7}
Provides:       rubygem(%{gem_name}) = %{version}
%endif

%description
Ruby/LDAP is an extension library for Ruby. It provides the interface to
some LDAP libraries (e.g. OpenLDAP, UMich LDAP, Netscape SDK,
ActiveDirectory). The common API for application development
is described in RFC1823 and is supported by Ruby/LDAP.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

# Well, this gem has some peculiar directory structure:
# Usually C extension files are under ext/%%gem_name,
# however this gem puts .c/.h files on the same directory
# of README or so...
# Once save the files to be installed to some other directory
rm -rf .INSTALL_FILES
mkdir .INSTALL_FILES
cp -a * .INSTALL_FILES
pushd .INSTALL_FILES
rm -rf \
	*.c \
	*.h \
	extconf.rb \
	%{nil}
popd

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
# special treatment: once clean up %%gem_instdir and
# install "clean" files
rm -rf %{buildroot}%{gem_instdir}
cp -a ./.INSTALL_FILES/ \
        %{buildroot}%{gem_instdir}/

mkdir -p %{buildroot}%{gem_extdir_mri}/
# TODO: move the extensions
mv ./%{gem_extdir_mri}/ldap* %{buildroot}%{gem_extdir_mri}/.
%if 0%{?fedora} >= 21
mv .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/.
%endif

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/extconf.rb/

%check
pushd .%{gem_instdir}

popd


%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}

%doc %{gem_instdir}/COPYING


%files doc
%doc %{gem_docdir}
#%%doc TODO README ChangeLog FAQ
%doc %{gem_instdir}/test
%doc %{gem_instdir}/win
%{gem_instdir}/ChangeLog
%{gem_instdir}/FAQ
%{gem_instdir}/NOTES
%{gem_instdir}/README
%{gem_instdir}/TODO



%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Vít Ondruch <vondruch@redhat.com> - 0.9.16-18
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.16-15
- F-30: rebuild against ruby26

* Fri Jul 27 2018 Vít Ondruch <vondruch@redhat.com> - 0.9.16-14
- Add "BR: gcc" to fix FTBFS (rhbz#1606148).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.9.16-12
- Rebuilt for switch to libxcrypt

* Wed Jan 03 2018 Vít Ondruch <vondruch@redhat.com> - 0.9.16-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.5

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 13 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.16-7
- F-26: rebuild for ruby24
- Some special treatment to files entry

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Vít Ondruch <vondruch@redhat.com> - 0.9.16-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.16-3
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Fri Dec 26 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.16-2
- Install gem.build_complete on F-21 (bug 1176450)

* Thu Sep 4 2014 Steve Traylen <steve.traylen@cern.ch> - 0.9.16-1
- New updstream 0.9.16, upstream moved to source and rubygems.org
- Update to ruby package guidelines.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 10 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.10-16
- F-19: rebuild for ruby 2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 07 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.10-13
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Apr 19 2010 Michael Stahnke <stahnma@fedoraproject.org> - 0.9.10-1
- new upstream version
- project URL and Source has changed

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.9.7-10
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 19 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0.9.7-8
- Fix FTBFS: Added ruby-ldap-0.9.7-openldap.patch

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 0.9.7-6
- rebuild with new openssl

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.7-5
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Michael Stahnke <mastahnke@gmail.com> - 0.9.7-4
- Bump for rebuild because of openldap bump

* Mon Oct 29 2007 Michael Stahnke <mastahnke@gmail.com> - 0.9.7-3
- More modifications from bug 346241

* Sun Oct 28 2007 Michael Stahnke <mastahnke@gmail.com> - 0.9.7-2
- Package modifications from bug 346241

* Mon Oct 22 2007 Michael Stahnke <mastahnke@gmail.com> - 0.9.7-1
- Initial Package for Fedora 
