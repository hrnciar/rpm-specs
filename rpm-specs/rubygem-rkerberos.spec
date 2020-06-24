# This package contains macros that provide functionality relating to
# Software Collections. These macros are not used in default
# Fedora builds, and should not be blindly copied or enabled.
# Specifically, the "scl" macro must not be defined in official Fedora
# builds. For more information, see:
# http://docs.fedoraproject.org/en-US/Fedora_Contributor_Documentation
# /1/html/Software_Collections_Guide/index.html
%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%global gem_name rkerberos

Summary: A Ruby interface for the the Kerberos library
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 0.1.5
Release: 17%{?dist}
License: Artistic 2.0
URL: http://github.com/domcleal/rkerberos
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
# Patch to compile with gcc8 + ruby 2.5 wrt rb_funcall argument num fix
Patch0:  rkerberos-0.1.5-gcc8-argnum-fix.patch

%if 0%{?scl} || 0%{?fedora} > 20
Requires: %{?scl_prefix}ruby
Requires: %{?scl_prefix}rubygems
%endif

BuildRequires: gcc
BuildRequires: %{?scl_prefix}ruby
BuildRequires: %{?scl_prefix}rubygems
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}ruby-devel
BuildRequires: krb5-devel
BuildRequires: %{?scl_prefix}rubygem-rake-compiler

%if 0%{?scl} || 0%{?fedora} > 20
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
%endif

#test
#BuildRequires: %{?scl_prefix}rubygem(test-unit)
#not yet in Fedora
#BuildRequires: %{?scl_prefix}rubygem(dbi-dbrc)

%description
The rkerberos library is an interface for the Kerberos 5 network
authentication protocol. It wraps the Kerberos C API.

%package doc
Summary: Documentation for rubygem-%{gem_name}
BuildArch: noarch

%description doc
This package contains documentation for rubygem-%{gem_name}.



%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}

%setup -q -D -T -n  %{gem_name}-%{version}
%patch0 -p1

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo.
rm -rf %{buildroot}%{gem_instdir}/ext

rm -rf %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/{ext,tmp}
rm -rf %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/.yardoc
rm -rf %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/Gemfile*
# rake-compiler isn't needed on the system itself
sed -i '/rake-compiler/ s/runtime/development/' %{buildroot}/%{gem_spec}

mkdir -p %{buildroot}%{_pkgdocdir}
for docfile in LICENSE README.md CHANGES MANIFEST; do
     mv %{buildroot}%{gem_instdir}/$docfile %{buildroot}%{_pkgdocdir}
     ln -s %{_pkgdocdir}/$docfile %{buildroot}%{gem_instdir}
done

%check
pushd ./%{gem_instdir}
# test do not work and many of them need functional keytab
# this need some work in upstream first
#testrb -v -Ilib -Itest test/test_*.rb
popd

%files
%doc %{_pkgdocdir}/README.md
%doc %{gem_instdir}/README.md
%doc %{_pkgdocdir}/LICENSE
%doc %{gem_instdir}/LICENSE
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{_pkgdocdir}/README.md
%doc %{gem_instdir}/README.md
%doc %{_pkgdocdir}/LICENSE
%doc %{gem_instdir}/LICENSE

%doc %{_pkgdocdir}/CHANGES
%doc %{gem_instdir}/CHANGES
%doc %{_pkgdocdir}/MANIFEST
%doc %{gem_instdir}/MANIFEST
%doc %{gem_docdir}
%{gem_instdir}/rkerberos.gemspec
%{gem_instdir}/test
%{gem_instdir}/Rakefile


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Vít Ondruch <vondruch@redhat.com> - 0.1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Vít Ondruch <vondruch@redhat.com> - 0.1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.5-11
- Patch to compile with gcc8 + ruby25 wrt rb_funcall argument num fix

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.1.5-9
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.5-8
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 07 2017 Vít Ondruch <vondruch@redhat.com> - 0.1.5-5
- Remove compilation workarounds (rhbz#1412274).

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.5-3
- Use GNU extension for compilar flag to avoid build failure on
  ppc64{,le} wrt kerberos header (bug 1412274)

* Thu Jan 12 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.1.5-2
- F-26: rebuild for ruby24
- add -D_DEFAULT_SOURCE for now

* Mon Oct 24 2016 Miroslav Suchý <msuchy@redhat.com> 0.1.5-1
- rebase to 0.1.5

* Thu Oct 22 2015 Miroslav Suchý <msuchy@redhat.com> 0.1.3-9
- rebuild due abi change of krb5 

* Mon May 26 2014 Miroslav Suchý <msuchy@redhat.com> 0.1.3-4
- move so lib directly to gem_extdir_mri and remove provides and requires
  which are automaticaly generated

* Wed Nov 20 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.3-3
- rebuild because of new krb-devel libraries 

* Mon Oct 21 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.3-2
- 1001728 - remove deps of -doc subpackage on main package

* Sun Sep 08 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.3-1
- rebase to 0.1.3 and move doc files to pkgdocdir
- 1001728 - use dist tag with question mark

* Tue Aug 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.2-3
- fix files section

* Tue Aug 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.1.2-2
- initial package

* Tue Jun 25 2013 Dominic Cleal <dcleal@redhat.com> 0.1.2-1
- Rebase to rkerberos 0.1.2 (dcleal@redhat.com)

* Thu May 23 2013 Dominic Cleal <dcleal@redhat.com> 0.1.1-4
- Remove rubygems version requirement (dcleal@redhat.com)

* Wed May 22 2013 Dominic Cleal <dcleal@redhat.com> 0.1.1-3
- Support building in non-SCL Ruby (dcleal@redhat.com)

* Tue May 21 2013 Martin Bačovský <mbacovsk@redhat.com> 0.1.1-2
- new package built with tito
- added support for SCL


* Wed May 08 2013 Dominic Cleal <dcleal@redhat.com> 0.1.1-1
- Update to 0.1.1 release
- Remove patch 103cea7d

* Wed May 08 2013 Dominic Cleal <dcleal@redhat.com> 0.1.0-1
- Initial 0.1.0 release
- Add patch 103cea7d (Add credential cache argument to get_init_creds_keytab)

