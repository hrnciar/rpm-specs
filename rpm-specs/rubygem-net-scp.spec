%global gem_name net-scp

Summary: A pure Ruby implementation of the SCP client protocol
Name: rubygem-%{gem_name}
Version: 1.2.1
Release: 13%{?dist}
License: MIT
URL: https://github.com/net-ssh/net-scp
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix test broken due to Net::SSH 4.0+.
# https://github.com/net-ssh/net-scp/pull/30
Patch0: net-scp-1.2.1-Fix-compatiblity-with-net-ssh-4.0.patch
# Fix Ruby 2.7 compatibility.
# https://github.com/net-ssh/net-scp/issues/50
Patch1: net-scp-1.2.1-Ruby-2.7-compatibilty.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(net-ssh)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(test-unit)
BuildArch: noarch

%description
A pure Ruby implementation of the SCP client protocol


%package doc
Summary: Documentation for %{name}
Requires:%{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep
%setup -q -n %{gem_name}-%{version}

%patch0 -p1
%patch1 -p1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install


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
%exclude %{gem_instdir}/.travis.yml
%{gem_libdir}
%doc %{gem_instdir}/LICENSE.txt
%exclude %{gem_cache}
%{gem_spec}

%files doc
%{gem_instdir}/Manifest
%{gem_instdir}/Rakefile
%{gem_instdir}/net-scp.gemspec
%{gem_instdir}/gem-public_cert.pem
%exclude %{gem_instdir}/setup.rb
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/CHANGES.txt
%{gem_instdir}/test
%doc %{gem_docdir}

%changelog
* Fri Apr 03 2020 Vít Ondruch <vondruch@redhat.com> - 1.2.1-13
- Fix the Ruby 2.7 compatibility (rhbz#1800021).

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Vít Ondruch <vondruch@redhat.com> - 1.2.1-6
- Fix FTBFS due to Net::SSH 4.0+ changes.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 11 2016 Vít Ondruch <vondruch@redhat.com> - 1.2.1-4
- Fix FTBFS due to incompatibility with latest net-ssh.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 17 2014 Vít Ondruch <vondruch@redhat.com> - 1.2.1-1
- Update to net-scp 1.2.1.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 09 2013 Vít Ondruch <vondruch@redhat.com> - 1.1.0-1
- Update to net-scp 1.1.0.

* Fri Mar 08 2013 Vít Ondruch <vondruch@redhat.com> - 1.0.4-7
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0.4-4
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 17 2011 Vít Ondruch <vondruch@redhat.com> - 1.0.4-2
- Removed obsolete cleanup.
- Removed explicit requires.

* Tue Feb 08 2011 Vít Ondruch <vondruch@redhat.com> - 1.0.4-1
- Initial package
