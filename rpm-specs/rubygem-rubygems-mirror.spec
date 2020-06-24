# Generated from rubygems-mirror-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rubygems-mirror

Name: rubygem-%{gem_name}
Version: 1.3.0
Release: 2%{?dist}
Summary: This is an update to the old `gem mirror` command
License: MIT
URL: https://github.com/rubygems/rubygems-mirror
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(builder)
BuildRequires: rubygem(net-http-persistent)
BuildArch: noarch

%description
This is an update to the old `gem mirror` command. It uses net/http/persistent
and threads to grab the mirror set a little faster than the original.
Eventually it will replace `gem mirror` completely. Right now the API is not
completely stable (it will change several times before release), however, I
will maintain stability in master.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}


%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Run the test suite
%check
pushd .%{gem_instdir}
ruby -Ilib -e 'Dir.glob "./test/test_*.rb", &method(:require)'

popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
# License is included in README file only
# https://github.com/rubygems/rubygems-mirror/pull/42
%doc %{gem_instdir}/README.rdoc
%exclude %{gem_instdir}/pkg

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/test
%doc %{gem_instdir}/Manifest.txt

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Pavel Valena <pvalena@redhat.com> - 1.3.0-1
- Update to rubygems-mirror 1.3.0.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Pavel Valena <pvalena@redhat.com> - 1.2.0-1
- Update to rubygems-mirror 1.2.0.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Pavel Valena <pvalena@redhat.com> - 1.1.0-1
- Initial package

