# Generated from regexp_parser-1.7.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name regexp_parser

Name: rubygem-%{gem_name}
Version: 1.7.1
Release: 1%{?dist}
Summary: Scanner, lexer, parser for ruby's regular expressions
License: MIT
URL: https://github.com/ammar/regexp_parser
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(regexp_property_values)
BuildRequires: ruby >= 1.9.1
BuildArch: noarch

%description
A library for tokenizing, lexing, and parsing Ruby regular expressions.


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
rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/regexp_parser.gemspec
%{gem_instdir}/spec

%changelog
* Tue May 26 2020 Pavel Valena <pvalena@redhat.com> - 1.7.1-1
- Initial package
