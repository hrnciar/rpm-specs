%global gem_name activeldap
%global do_check 0

%if 0%{?fedora} < 19
%global rubyabi 1.9.1
%endif

Summary:        Ruby/ActiveLdap is a object-oriented API to LDAP
Name:           rubygem-%{gem_name}
Version:        5.2.4
Release:        3%{?dist}
# Overall license: GPLv2+ or Ruby
# test-unit/: GPLv2 or Ruby
License:        (GPLv2+ or Ruby) and (GPLv2 or Ruby)
URL:            http://activeldap.github.io/
Source0:        http://rubygems.org/downloads/%{gem_name}-%{version}.gem
%if 0%{?fedora} >= 19
Requires:	ruby(release)
BuildRequires:	ruby(release)
%else
Requires:	ruby(abi) = %{rubyabi}
Requires:	ruby 
BuildRequires:	ruby(abi) = %{rubyabi}
BuildRequires:	ruby 
%endif

BuildRequires:  rubygems-devel
BuildRequires:  gettext

%if %{do_check}
BuildRequires:		rubygem(activemodel) >= 4.0.0
BuildRequires:		rubygem(locale)
BuildRequires:		rubygem(gettext)
BuildRequires:		rubygem(gettext_i18n_rails)
BuildRequires:		rubygem(test-unit)
%endif

%if 0%{?fedora} < 21
Requires:		rubygem(activemodel) >= 4.0.0
Requires:		rubygem(locale)
Requires:		rubygem(gettext)
Requires:		rubygem(gettext_i18n_rails)
%endif
BuildArch:      noarch
Provides:       rubygem(%{gem_name}) = %{version}-%{release}

%description
'Ruby/ActiveLdap' is a ruby extension library which provides a clean objected
oriented interface to the Ruby/LDAP library.  It was inspired by ActiveRecord.
This is not nearly as clean or as flexible as ActiveRecord, but it is still
trivial to define new objects and manipulate them with minimal difficulty.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains documentation for %{name}.

%prep
%setup -q -c -T

# Gem repack
TOPDIR=$(pwd)
mkdir tmpunpackdir
pushd tmpunpackdir

gem unpack %{SOURCE0}
cd %{gem_name}-%{version}
gem specification -l --ruby %{SOURCE0} > %{gem_name}.gemspec
gem build %{gem_name}.gemspec
mv %{gem_name}-%{version}.gem $TOPDIR

popd
rm -rf tmpunpackdir

%build
%gem_install

# Permission
find . -type f -print0 | xargs --null chmod go-w

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# cleanups
rm -f %{buildroot}%{gem_instdir}/.yardopts

%check
# Setup for LDAP server is needed, skip
exit 0

%files
%dir	%{gem_instdir}
%doc	%{gem_instdir}/[A-Z]*
%{gem_instdir}/lib/

%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%{gem_instdir}/benchmark/
%{gem_instdir}/doc/
%{gem_instdir}/examples/
%{gem_instdir}/po/
%{gem_instdir}/test/
%{gem_dir}/doc/%{gem_name}-%{version}/

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 31 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.2.4-1
- 5.2.4

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr  6 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.1.1-1
- 5.1.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan  2 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.1.0-1
- 5.1.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May  5 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.6-1
- 4.0.6

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.5-1
- 4.0.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec  5 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.4-1
- 4.0.4

* Fri Jul 04 2014 Josef Stribny <jstribny@redhat.com> - 4.0.3-1
- Update to 4.0.3
- Update project URLs
- Add support for Ruby on Rails 4.1.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 15 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.2-1
- 4.0.2

* Wed Nov 13 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.1-1
- 4.0.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.2-4
- Cleanup

* Mon Mar 18 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.2-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov  2 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 3.2.2-1
- Update to 3.2.2

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Sep 11 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.2-1
- Update to 1.2.2
- Split out document files

* Mon Feb 15 2010 Darryl L. Pierce <dpierce@redhat.com> - 1.2.1-1
- Upgraded dependency on rubygem-activerecord to >= 2.3.5.
- Upgraded dependency on rubygem-locale to >= 2.0.5.
- Upgraded dependency on rubygem-gettext to >= 2.1.0.
- Upgraded dependency on rubygem-gettext_activerecord to >= 2.1.0.
- Upgraded dependency on rubygem-hoe to >= 2.4.0
- Release 1.2.1 of ActiveLDAP.

* Fri Dec  4 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.0-4
- Change the dependency against locale/gettext/active*
  from "strictly equal (=)" to "not less than (>=)"
  (bug 542917)

* Tue Sep 22 2009 Darryl L. Pierce <dpierce@redhat.com> - 1.2.0-1
- Release 1.2.0 of ActiveLDAP.
- Changed dependency on rubygem-activerecord to be >= 2.3.4
- Changed dependency on rubygem-hoe to be >= 2.3.3
- Added new l12n files to spec.

* Thu Jul 30 2009 Darryl L. Pierce <dpierce@redhat.com> - 1.1.0-3
- Changed dependency on rubygem-activerecord to be >= 2.3.2.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Darryl L. Pierce <dpierce@redhat.com> - 1.1.0-1
- Release 1.1.0 of ActiveLdap.
- Dependency on rubygem-hoe changed to 2.3.2.
- Dependency on rubygem-activerecord changed to 2.3.2.
- Dependency on rubygem-locale added.
- Dependency on rubygem-gettext added.
- Dependency on rubygem-gettext_activerecord added.

* Fri Jun  5 2009 Darryl L. Pierce <dpierce@redhat.com> - 1.0.9-1
- Release 1.0.9 of ActiveLdap.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Darryl L. Pierce <dpierce@redhat.com> - 1.0.2-1
- Release 1.0.2 of ActiveLdap.

* Tue Jun 17 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.0.1-1
- Release 1.0.1 of the gem.

* Mon Jun 09 2008 Darryl L. Pierce <dpierce@redhat.com> - 1.0.0-1
- Release 1.0.0 of the gem.

* Thu May 15 2008 Darryl L. Pierce <dpierce@redhat.com> - 0.10.0-10
- First official build for rawhide.

* Mon May 12 2008 Darryl L. Pierce <dpierce@redaht.com> - 0.10.0-9
- First build updated for Fedora.

* Tue Apr 29 2008 Darryl L. Pierce <dpierce@redhat.com> - 0.10.0-8
- Missed a script.

* Tue Apr 29 2008 Darryl L. Pierce <dpierce@redhat.com> - 0.10.0-7
- Fixing three scripts to be executable.

* Tue Apr 29 2008 Darryl L. Pierce <dpierce@redhat.com> - 0.10.0-6
- Fixed the shebang in all scripts to remove an implied dependency on /usr/bin/ruby1.8

* Mon Apr 28 2008 Darryl L. Pierce <dpierce@redhat.com> - 0.10.0-5
- Added requirement for ruby-ldap

* Mon Apr 28 2008 Darryl L. Pierce <dpierce@redhat.com> - 0.10.0-4
- Moved all macro definitions to the top of the spec file.

* Mon Apr 28 2008 Darryl L. Pierce <dpierce@redhat.com> - 0.10.0-3
- Modified the spec to fix rpmlint errors

* Mon Apr 28 2008 Darryl L. Pierce <dpierce@redhat.com> - 0.10.0-2
- Fixed the spec file to comply with packaging guidelines

* Fri Apr 18 2008 Darryl L. Pierce <dpierce@redhat.com> - 0.10.0-1
- Initial package
