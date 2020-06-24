# Generated from qpid_proton-0.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name qpid_proton
%global proton_version 0.31.0
%global optflags %(echo %{optflags} | sed 's/-Wall/-Wall -Wno-unused-variable -Wno-unused-function/')

%{!?gem_extdir_mri: %global gem_extdir_mri %{_libdir}/gems/ruby/%{gem_name}-%{version}}

Summary:       Ruby language bindings for the Qpid Proton messaging framework
Name:          rubygem-%{gem_name}
Version:       %{proton_version}
Release:       1%{?dist}
License:       ASL 2.0

URL:           http://qpid.apache.org/proton
Source0:       http://rubygems.org/gems/%{gem_name}-%{proton_version}.gem
Source1:       licenses.xml

%if 0%{?fedora} > 0
BuildRequires: ruby(release)
%endif

BuildRequires: ruby-devel
BuildRequires: rubygems-devel
BuildRequires: qpid-proton-c-devel >= %{proton_version}
BuildRequires: libuuid-devel
BuildRequires: swig
BuildRequires: gcc
BuildRequires: make

Requires:      qpid-proton-c >= %{proton_version}


%description
Proton is a high performance, lightweight messaging library. It can be used in
the widest range of messaging applications including brokers, client libraries,
routers, bridges, proxies, and more. Proton is based on the AMQP 1.0 messaging
standard.


%package doc
Summary:   Documentation for %{name}

# RHEL6 rdoc doesn't seem to work well with noarch doc packages
%if 0%{?rhel} != 6
BuildArch: noarch
%endif

%description doc
%{summary}.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# apply any patches here


%build
gem build %{gem_name}.gemspec
%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}

%if 0%{?fedora} > 20
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/
%endif

install -pm 644 %{SOURCE1} %{buildroot}%{gem_instdir}/
rm -rf %{buildroot}%{gem_instdir}/ext


%check


%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/licenses.xml
%doc %{gem_instdir}/examples
%doc %{gem_instdir}/tests

%files doc
%doc %{gem_docdir}

%changelog
* Thu May 14 2020 Irina Boverman <iboverma@redhat.com> - 0.31.0-1
- Rebased to 0.31.0

* Tue Feb  4 2020 Irina Boverman <iboverma@redhat.com> - 0.30.0-1
- Rebased to 0.30.0

* Sat Jan 18 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.29.0-2
- F-32: rebuild against ruby27

* Wed Oct  2 2019 Irina Boverman <iboverma@redhat.com> - 0.29.0-1
- Rebased to 0.29.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Irina Boverman <iboverma@redhat.com> - 0.28.0-1
- Rebased to 0.28.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Vít Ondruch <vondruch@redhat.com> - 0.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Tue Jan  8 2019 Irina Boverman <iboverma@redhat.com> - 0.26.0-1
- Rebased to 0.26.0

* Tue Jul 24 2018 Irina Boverman <iboverma@redhat.com> - 0.24.0-1
- Rebased to 0.24.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 13 2018 Irina Boverman <iboverma@redhat.com> - 0.21.0-1
- Rebased to 0.21.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.18.1-3
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.18.1-2
- F-28: rebuild for ruby25

* Thu Nov 16 2017 Irina Boverman <iboverma@redhat.com> - 0.18.1-1
- Rebased to 0.18.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Irina Boverman <iboverma@redhat.com> - 0.17.0-1
- Rebased to 0.17.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Vít Ondruch <vondruch@redhat.com> - 0.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Wed Oct 19 2016 Kalev Lember <klember@redhat.com> - 0.14.0-2
- Rebuilt for libqpid-proton soname bump

* Tue Sep  6 2016 Irina Boverman <iboverma@redhat.com> - 0.14.0-1
- Rebased to 0.14.0

* Tue Jun 28 2016 Irina Boverman <iboverma@redhat.com> - 0.13.0-1
- Rebased to 0.13.0

* Wed Mar 23 2016 Irina Boverman <iboverma@redhat.com> - 0.12.0-1
- Rebased to 0.12.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Vít Ondruch <vondruch@redhat.com> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Thu Sep 10 2015 Irina Boverman <iboverma@redhat.com> - 0.10.1-1
- Rebased to 0.10.1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr  7 2015 Darryl L. Pierce <dpierce@redhat.com> - 0.9-1
- Rebased on qpid_proton 0.9.0.
- Added dependency on rubygem(json).

* Fri Jan 16 2015 Vít Ondruch <vondruch@redhat.com> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Wed Nov 19 2014 Darryl L. Pierce <dpierce@redhat.com> - 0.8-1
- Rebased on Proton 0.8.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 15 2014 Darryl L. Pierce <dpierce@redhat.com> - 0.7-4
- Removed intra-package comments.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May  1 2014 Darryl L. Pierce <dpierce@redhat.com> - 0.7-2
- Made the -doc package arch-specific for EL6 due to rdoc issues.

* Wed Apr 30 2014 Darryl L. Pierce <dpierce@redhat.com> - 0.7-1
- Rebased on Proton 0.7.

* Tue Apr 15 2014 Vít Ondruch <vondruch@redhat.com> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Mon Feb 10 2014 Darryl L. Pierce <dpierce@redhat.com> - 0.6-2
- Removed requirement on the main package by the doc subpackage.
- Removed Group declarations.

* Fri Jan 17 2014 Darryl L. Pierce <dpierce@redhat.com> - 0.6-1
- Rebased on Proton 0.6.

* Thu Aug 29 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.5-1
- Rebased on Proton 0.5.

* Mon Apr  1 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.4-2.2
- Fixed the dependencies to be qpid-proton-c and qpid-proton-c-devel.

* Wed Mar  6 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.4-2.1
- Changed ruby(release) to ruby(abi) for Fedora < 19.
- Resolves: BZ#906843

* Wed Mar  6 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.4-2
- First official build for Fedora.
- Resolves: BZ#906843

* Sat Mar  2 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.4-1.1
- Changed the BR for Ruby to match F19 packaging guidelines.
- Changed install to use the gem_install macro.
- Fixed the installation of the native library.

* Fri Mar  1 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.4-1
- Rebased on Proton 0.4.

* Mon Feb 25 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.3-1.1
- Updated to meet the new Fedora 19 packaging guidelines.

* Fri Feb  1 2013 Darryl L. Pierce <dpierce@redhat.com> - 0.3-1
- Initial package
