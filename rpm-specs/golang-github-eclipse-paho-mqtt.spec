# Generated by go2rpm 1
# Needs network
%bcond_with check

# https://github.com/eclipse/paho.mqtt.golang
%global goipath         github.com/eclipse/paho.mqtt.golang
Version:                1.2.0

%gometa

%global common_description %{expand:
This code builds a library which enable applications to connect to an MQTT
broker to publish messages, and to subscribe to topics and receive published
messages.}

%global golicenses      LICENSE edl-v10 epl-v10
%global godocs          CONTRIBUTING.md README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Eclipse Paho MQTT Go client

License:        EPL-1.0 or BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/net/proxy)
BuildRequires:  golang(golang.org/x/net/websocket)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Fri Jan 31 23:34:52 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.0-1
- Initial package