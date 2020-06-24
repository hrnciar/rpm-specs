# Generated from ruby-dbus-0.7.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name ruby-dbus

Name: rubygem-%{gem_name}
Version: 0.11.0
Release: 9%{?dist}
Summary: Ruby module for interaction with D-Bus
# MIT: lib/dbus/core_ext/*
License: LGPLv2+ and MIT
URL: https://trac.luon.net/ruby-dbus
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-ruby-dbus-0.11.0-RSpec-3-compatibility.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(nokogiri)
BuildRequires: %{_bindir}/dbus-daemon
BuildArch: noarch

%description
Ruby D-Bus provides an implementation of the D-Bus protocol such that the
D-Bus system can be used in the Ruby programming language.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

pushd .%{gem_instdir}
%patch0 -p1
popd

# fix rpmlint issue with Rakefile (should not have shebang)
sed -i '1d' .%{gem_instdir}/Rakefile

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}/test/tools
./test_env rspec ../../test/
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/COPYING
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/NEWS
%doc %{gem_instdir}/README.md
%{gem_instdir}/VERSION
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/doc
%{gem_instdir}/examples
%{gem_instdir}/ruby-dbus.gemspec
%{gem_instdir}/test

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 01 2015 Vít Ondruch <vondruch@redhat.com> - 0.11.0-1
- Update to ruby-dubs 0.11.0.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.0-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Mon Feb 18 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.0-1
- Update to 0.9.0.
- Don't run tests by default (fail on Koji because of no networking).

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 05 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.8.0-1
- Update to 0.8.0.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 26 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.0-3
- Bump release to allow getting 0.7.0-3 into F16 (stupid mistake).

* Tue Feb 28 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.0-2
- Simplified the test running.
- Properly obsolete ruby-dbus.
- Applied the patch that unbundles files from activesupport (accepted by upstream).

* Tue Feb 28 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.0-1
- Initial package
