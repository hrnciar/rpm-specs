%global gem_name snmp

Summary: A Ruby implementation of SNMP (the Simple Network Management Protocol)
Name: rubygem-%{gem_name}
Version: 1.2.0
Release: 11%{?dist}
# https://github.com/hallidave/ruby-snmp/issues/11
License: GPLv2 or Ruby
URL: http://snmplib.rubyforge.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix unstable TestVarBind#test_integer_create_from_string test.
# https://github.com/hallidave/ruby-snmp/commit/9d218af630d0ee6178a0529337e8759a4c40a747
Patch0: snmp-1.2.0-Fully-qualify-SNMP-Integer-class.patch
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: rubygem(minitest) > 5
BuildArch: noarch

%description
A Ruby implementation of SNMP (the Simple Network Management Protocol).

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

pushd .%{gem_instdir}
%patch0 -p1
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ruby -Ilib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/data
%doc %{gem_instdir}/Rakefile
%doc %{gem_docdir}
%doc %{gem_instdir}/examples
%doc %{gem_instdir}/test
%doc %{gem_instdir}/README.rdoc
%exclude %{gem_cache}
%{gem_spec}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Vít Ondruch <vondruch@redhat.com> - 1.2.0-4
- Fix unstable TestVarBind#test_integer_create_from_string test.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 10 2014 Michael Stahnke <stahnma@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0 as per 1120178

* Mon Jul 14 2014 Vít Ondruch <vondruch@redhat.com> - 1.1.1-1
- Update to snmp 1.1.1.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 12 2013 Vít Ondruch <vondruch@redhat.com> - 1.1.0-7
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 08 2012 Vít Ondruch <vondruch@redhat.com> - 1.1.0-4
- Fix broken dependencies.

* Fri Feb 03 2012 Vít Ondruch <vondruch@redhat.com> - 1.1.0-3
- Rebuilt for Ruby 1.9.3.

* Sun Jan 08 2012 <stahnma@fedoraproject.org> - 1.1.0-2
- Ensure %%check can run properly

* Sun Jan 08 2012 <stahnma@fedoraproject.org> - 1.1.0-1
- Fix FTBFS bug  715639

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jun 10 2010 Michael Stahnke <stahnma@fedoraproject.org> - 1.0.3-1
- New version

* Mon May 24 2010 Michael Stahnke <stahnma@fedoraproject.org> - 1.0.2-1
- Fixes from review bug #587438
- Initial package
