%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name wirb
Summary: Wavy IRB: Colorizes irb results
Name: %{?scl_prefix}rubygem-%{gem_name}

Version: 2.1.1
Release: 7%{dist}
License: MIT
URL: https://github.com/janlelis/wirb
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems
BuildArch: noarch
#tests
BuildRequires: rubygem(rspec)

%description
Wavy IRB: Colorizes irb results. It originated from Wirble, but only provides
result highlighting. Just call Wirb.start and enjoy the colors in your IRB ;).
You can use it with your favorite colorizer engine. See README.md for more
details.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

%{?scl:scl enable %{scl} - << \EOF}
%if 0%{?fedora} >= 18
%{gem_install}
%else
mkdir -p ./%{gem_dir}
gem install --local --install-dir ./%{gem_dir} --force %{SOURCE0}
%endif
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

rm -rf %{buildroot}%{gem_instdir}/.yardoc
rm -f %{buildroot}%{gem_instdir}/.gemtest

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/data
%license %{gem_instdir}/COPYING.txt
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/README.md

%files doc
%{gem_instdir}/spec
%doc %{gem_docdir}
%doc %{gem_instdir}/CODE_OF_CONDUCT.md
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec

%check
pushd ./%{gem_instdir}
#requires rubygem-zucker which is not in Fedora
#rspec spec
popd

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Dominic Cleal <dominic@cleal.org> - 2.1.1-1
- rebase to wirb-2.1.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Miroslav Suchý <msuchy@redhat.com> 2.0.0-1
- rebase to wirb-2.0.0
- Fix spurious Requires and also kill explicit Requires on F-21+

* Tue Feb 11 2014 Miroslav Suchý <msuchy@redhat.com> 1.0.3-1
- rebase to wirb-1.0.3

* Fri Aug 30 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.1-5
- 998915 - move README to main package
- macro gem_install is available even in F18
- 998915 - use virtual BR
- 998915 - add full source url

* Tue Aug 20 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.1-4
- populate ./%%{gem_dir} so we can cd there for tests

* Tue Aug 20 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.1-3
- use standard group
- summary should not end with dot

* Tue Aug 20 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.1-2
- add placeholder for tests

* Tue Aug 20 2013 Miroslav Suchý <msuchy@redhat.com> 1.0.1-1
- rebase to 1.0.1

* Thu Jul 04 2013 Dominic Cleal <dcleal@redhat.com> 0.4.2-6
- change ruby(abi) to ruby(release) for F19+ (dcleal@redhat.com)
- delete all zero sized tito.props (msuchy@redhat.com)
- with recent tito you do not need SCL meta package (msuchy@redhat.com)

* Wed Mar 27 2013 Miroslav Suchý <msuchy@redhat.com> 0.4.2-4
- put correct license in spec (msuchy@redhat.com)

* Thu Mar 14 2013 Miroslav Suchý <msuchy@redhat.com> 0.4.2-3
- new package built with tito

* Fri Sep 07 2012 Miroslav Suchý <msuchy@redhat.com> 0.4.2-2
- polish the spec (msuchy@redhat.com)

* Thu Sep 06 2012 Miroslav Suchý <msuchy@redhat.com> 0.4.2-1
- new package built with tito

