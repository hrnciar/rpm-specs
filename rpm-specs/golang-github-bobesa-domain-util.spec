# Generated by go2rpm 1
%bcond_without check

# https://github.com/bobesa/go-domain-util
%global goipath         github.com/bobesa/go-domain-util
%global commit          4033b5f7dd89ff01908ec97cb7a367a81fe4f6d7

%gometa

%global common_description %{expand:
Handler for URL parts and identification of TLD and sub domains.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        0.1%{?dist}
Summary:        Handler for URLs and identification of TLD and sub domains

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/net/idna)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Mon Mar 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0-0.1.20200330git4033b5f
- Initial package
