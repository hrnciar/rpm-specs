%global gem_name net-sftp

Summary: A pure Ruby implementation of the SFTP client protocol
Name: rubygem-%{gem_name}
Version: 2.1.2
Release: 11%{?dist}
License: MIT or LGPLv2
URL: https://github.com/net-ssh/net-sftp
Source0: http://rubygems.org/downloads/%{gem_name}-%{version}.gem
# Fix the test suite to be compatible with MiniTest 5.x.
# https://github.com/net-ssh/net-sftp/pull/37
Patch0: rubygem-net-sftp-2.1.2-Move-to-Minitest-5.patch
# Fix test broken by Net::SSH 4.0+.
# https://github.com/net-ssh/net-sftp/pull/59
Patch1: net-sftp-2.1.2-Fix-compatiblity-with-net-ssh-4.0.patch
# Fix Ruby 2.4 compatibility.
# https://github.com/net-ssh/net-sftp/pull/60
Patch2: net-sftp-2.1.2-Fix-Ruby-2.4-compatibility.patch

BuildRequires: rubygems-devel
BuildRequires: rubygem(minitest) > 5
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(net-ssh)
BuildArch: noarch

%description
A pure Ruby implementation of the SFTP client protocol

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

pushd .%{gem_instdir}
%patch0 -p1
%patch1 -p1
%patch2 -p1
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ruby -Itest test/test_all.rb
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/CHANGES.txt
%doc %{gem_instdir}/LICENSE.txt
%doc %{gem_instdir}/Manifest
%doc %{gem_instdir}/README.rdoc
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/test
%{gem_instdir}/Rakefile
%{gem_instdir}/gem-public_cert.pem
%{gem_instdir}/net-sftp.gemspec
%doc %{gem_docdir}
# License: LGPL version 2.1
%{gem_instdir}/setup.rb

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Vít Ondruch <vondruch@redhat.com>
- Fix compatibility with Net::SSH 4.0+.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jul 15 2014 Vít Ondruch <vondruch@redhat.com> - 2.1.2-1
- Update to net-sftp 2.1.2.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 18 2013 Vít Ondruch <vondruch@redhat.com> - 2.1.1-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to net-sftp 2.1.1.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 03 2012 Vít Ondruch <vondruch@redhat.com> - 2.0.5-5
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 14 2010 Michal Fojtik <mfojtik@redhat.com> - 2.0.5-2
- Fixed license
- Fixes source0 URL

* Wed Oct 13 2010 Michal Fojtik <mfojtik@redhat.com> - 2.0.5-1
- Initial package
