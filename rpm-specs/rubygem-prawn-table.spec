%global gem_name prawn-table

Name: rubygem-%{gem_name}
Version: 0.2.2
Release: 11%{?dist}
Summary: Provides tables for PrawnPDF
License: Ruby or GPLv2 or GPLv3
URL: https://github.com/prawnpdf/prawn-table
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygem(prawn) >= 1.3.0
# data/images/prawn.png is required by test suite.
BuildRequires: rubygem-prawn-doc
BuildRequires: rubygem(pdf-inspector) => 1.1.0
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(pdf-reader) => 1.2
BuildArch: noarch

%description
Prawn::Table provides tables for the Prawn PDF toolkit.

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

%check
pushd .%{gem_instdir}
sed -i '/^require "bundler"/d' ./spec/spec_helper.rb
sed -i '/^Bundler.setup/d' ./spec/spec_helper.rb
# Don't run unresolved test cases.
# https://github.com/prawnpdf/prawn-table/blob/master/Rakefile#L15
# 4 failures expected due to image file not included in prawn gem
rspec spec -t ~unresolved \
  | tee /dev/stderr \
  | grep '222 examples, 4 failures'
# Currently disabled
# rspec2 spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/COPYING
%license %{gem_instdir}/GPLv2
%license %{gem_instdir}/GPLv3
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_instdir}/manual
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/prawn-table.gemspec
%{gem_instdir}/spec

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Christopher Brown <chris.brown@redhat.com> - 0.2.2-8
- Add test suite workaround due to missing image in prawn

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 27 2018 Vít Ondruch <vondruch@redhat.com> - 0.2.2-6
- Remove restriction on BR.

* Tue Feb 27 2018 Vít Ondruch <vondruch@redhat.com> - 0.2.2-5
- Enable test suite.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jun 17 2016 Fabio Alessandro Locati <me@fale.io> - 0.2.2-1
- Initial package
